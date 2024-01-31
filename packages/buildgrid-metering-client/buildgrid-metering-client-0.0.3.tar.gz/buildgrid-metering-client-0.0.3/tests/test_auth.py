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

from unittest import mock

import pytest

from buildgrid_metering.client.auth import AuthTokenConfig, AuthTokenLoader, AuthTokenMode
from buildgrid_metering.client.exceptions import MeteringServiceClientError


@pytest.mark.asyncio
async def test_auth_loader_constant():
    # GIVEN
    config = AuthTokenConfig(AuthTokenMode.CONSTANT, "sometoken")
    loader = AuthTokenLoader(config)

    # WHEN
    token = loader.get_token()

    # THEN
    assert token == "sometoken"


@pytest.mark.asyncio
async def test_auth_loader_none():
    # GIVEN
    config = AuthTokenConfig(AuthTokenMode.NONE, "")
    loader = AuthTokenLoader(config)

    # WHEN
    token = loader.get_token()

    # THEN
    assert token is None


@pytest.mark.asyncio
@mock.patch("buildgrid_metering.client.auth.open")
async def test_auth_loader_filepath(mock_open_file):
    # GIVEN
    mock_token_file = mock.MagicMock()
    mock_token_file.read.return_value = "sometoken"
    mock_open_file.return_value.__enter__.return_value = mock_token_file

    config = AuthTokenConfig(AuthTokenMode.FILEPATH, "/tmp/token")
    loader = AuthTokenLoader(config)

    # WHEN
    token = loader.get_token()

    # THEN
    assert token == "sometoken"


@pytest.mark.asyncio
@mock.patch("buildgrid_metering.client.auth.open")
async def test_auth_loader_filepath_not_readable(mock_open_file):
    # GIVEN
    mock_open_file.return_value.__enter__.side_effect = OSError("cannot open file")

    config = AuthTokenConfig(AuthTokenMode.FILEPATH, "/tmp/nottoken")
    loader = AuthTokenLoader(config)

    # WHEN
    with pytest.raises(MeteringServiceClientError):
        await loader.get_token()
