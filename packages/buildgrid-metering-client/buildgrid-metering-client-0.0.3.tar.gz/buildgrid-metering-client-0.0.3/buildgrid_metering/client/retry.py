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


from dataclasses import dataclass
from typing import Tuple, Type


@dataclass(frozen=True)
class RetryConfig:
    """RetryConfig for MeteringServiceClient"""

    max_attempts: int = 0
    """Max attempts to retry the API call. Default to 0 (no retry)."""
    exp_base: float = 1.5
    """Exponential base before retry. Default to 1.5"""
    multiplier: float = 1.0
    """Multiplier for exponential back-off. Defaults to 1.0"""
    max_wait: float = 30.0
    """Maximum of wait time in seconds between retries. Default to 30.0"""
    http_statuses: Tuple[int, ...] = ()
    """HTTP status codes to retry, e.g. 503. Default to empty."""
    exception_types: Tuple[Type[Exception], ...] = ()
    """Exception types to retry. Default to empty."""
    cause_exception_types: Tuple[Type[Exception], ...] = ()
    """Cause exception types to retry. Default to empty."""
