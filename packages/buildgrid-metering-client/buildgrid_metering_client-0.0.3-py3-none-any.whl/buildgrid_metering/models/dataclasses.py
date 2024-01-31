# Copyright (C) 2023 Bloomberg LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import abc
from typing import Dict, TypeVar, Union

from pydantic import BaseModel


class Identity(BaseModel):
    """Identity that consumes build resource

    Args:
        Instance: REAPI service instance, e.g., "dev"
        Workflow: The associated workflow of the operation, e.g., "build"
        Actor: The tooling or agent that submitted the operation, e.g., "my-build-tool"
        Subject: The end user that submitted the operation, e.g. "user1"
    """

    instance: str
    workflow: str
    actor: str
    subject: str


R = TypeVar("R", bound="ResourceUsage")


class ResourceUsage(BaseModel, abc.ABC):
    @abc.abstractmethod
    def combine(self: R, other: R) -> R:
        """Combine two resource usages of the same type"""

    @abc.abstractmethod
    def get_throttled(self: R, threshold: R) -> R:
        """Get a subset of this resource type that exceeds the predefined threshold
        while attributes that are <= threshold are default-valued."""

    def __add__(self: R, other: R) -> R:
        return self.combine(other)


N = TypeVar("N", bound="NumericResourceUsage")


class NumericResourceUsage(ResourceUsage):
    """A subtype of ResourceUsage where each attribute is either int or float.
    It provides reasonable default methods.
    """

    def combine(self: N, other: N) -> N:
        self_dict = self.dict(exclude_unset=True)
        other_dict = other.dict(exclude_unset=True)

        combined_dict: Dict[str, Union[int, float]] = {
            attr: self_dict.get(attr, 0) + other_dict.get(attr, 0) for attr in self_dict.keys() | other_dict.keys()
        }

        return type(self)(**combined_dict)

    def get_throttled(self: N, threshold: N) -> N:
        threshold_dict = threshold.dict(exclude_unset=True)
        self_dict = self.dict()

        throttled = {k: self_dict[k] for k, v in threshold_dict.items() if self_dict[k] > v}

        return type(self)(**throttled)


class ComputingUsage(NumericResourceUsage):
    """Basic computing resource usage defined in getrusage(2)"""

    utime: int = 0
    stime: int = 0
    maxrss: int = 0
    inblock: int = 0
    oublock: int = 0


class CASUsage(NumericResourceUsage):
    """IO usage of ContentAddressableStorage"""

    read_bytes: int = 0
    write_bytes: int = 0


class Usage(ResourceUsage):
    """
    The aggregation of all kinds of usages
    """

    computing: ComputingUsage = ComputingUsage()
    cas: CASUsage = CASUsage()

    def combine(self, other: Usage) -> Usage:
        computing = self.computing + other.computing
        cas = self.cas + other.cas

        return Usage(computing=computing, cas=cas)

    def get_throttled(self: Usage, threshold: Usage) -> Usage:
        computing = self.computing.get_throttled(threshold.computing)
        cas = self.cas.get_throttled(threshold.cas)

        return Usage(computing=computing, cas=cas)

    def __str__(self) -> str:
        return f"computing: [ {self.computing} ], cas: [ {self.cas} ]"
