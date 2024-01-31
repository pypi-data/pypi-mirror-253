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
from enum import Enum
from typing import Optional

from cachetools.func import ttl_cache

from buildgrid_metering.client.exceptions import MeteringServiceClientError


class AuthTokenMode(str, Enum):
    CONSTANT = "constant"
    FILEPATH = "filepath"
    NONE = "none"


@dataclass
class AuthTokenConfig:
    """Config on how to load the JWT token.
    if `mode == CONSTANT`, the token will always be the `value`
    if `mode == FILEPATH`, it reads the file located at `value`
    if `mode == NONE`, it returns `None`
    """

    mode: AuthTokenMode
    value: str


class AuthTokenLoader:
    """A class that loads JWT authentication token based on the config"""

    _config: AuthTokenConfig

    def __init__(self, config: AuthTokenConfig) -> None:
        self._config = config

    def get_token(self) -> Optional[str]:
        """Get the JWT authentication token

        Raises:
            ValueError: if the `mode` is not supported

        Returns:
            str | None: JWT if `mode` is not NONE
        """
        if self._config.mode == AuthTokenMode.NONE:
            return None
        if self._config.mode == AuthTokenMode.CONSTANT:
            return self._config.value
        if self._config.mode == AuthTokenMode.FILEPATH:
            return _load_token_from_file(self._config.value)
        raise ValueError(f"Unsupported AuthTokenMode: {self._config.mode}")


@ttl_cache(maxsize=1, ttl=60 * 60)
def _load_token_from_file(path: str) -> str:
    try:
        with open(path, mode="r") as token_file:
            return token_file.read().strip()
    except Exception as e:
        raise MeteringServiceClientError(f"Cannot read token from filepath: {path}") from e
