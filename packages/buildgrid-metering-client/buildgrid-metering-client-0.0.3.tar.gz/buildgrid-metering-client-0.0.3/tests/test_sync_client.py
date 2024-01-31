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
import requests

from buildgrid_metering.client.auth import AuthTokenConfig, AuthTokenLoader, AuthTokenMode
from buildgrid_metering.client.client import SyncMeteringServiceClient
from buildgrid_metering.client.exceptions import MeteringServiceClientError, MeteringServiceHTTPError
from buildgrid_metering.client.retry import RetryConfig
from buildgrid_metering.models.api import GetThrottlingResponse
from buildgrid_metering.models.dataclasses import ComputingUsage, Identity, Usage

MOCK_IDENTITY = Identity(instance="dev", workflow="build", actor="tool", subject="username")
MOCK_USAGE = Usage(computing=ComputingUsage(utime=123))


@pytest.fixture
def mock_http_session():
    with mock.patch("buildgrid_metering.client.client.requests.Session") as session_cls:
        session = mock.MagicMock()
        session_cls.return_value.__enter__.return_value = session
        yield session


@pytest.fixture
def client():
    token_loader = AuthTokenLoader(AuthTokenConfig(AuthTokenMode.CONSTANT, "token"))
    yield SyncMeteringServiceClient("http://localhost:8000", token_loader)


def test_put_usage(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    mock_response = mock.Mock
    mock_response.status_code = 204
    mock_http_session.put.return_value = mock_response

    # WHEN
    client.put_usage(MOCK_IDENTITY, "op", MOCK_USAGE)

    # THEN
    # no exception is raised


def test_put_usage_unprocessable_content(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    mock_response = mock.Mock()
    mock_response.status_code = 422
    mock_response.context = b"request cannot be validated"
    mock_http_session.put.return_value = mock_response

    # WHEN
    with pytest.raises(MeteringServiceHTTPError) as e:
        client.put_usage(MOCK_IDENTITY, "op", MOCK_USAGE)

    # THEN
    assert e.value.http_status == 422


def test_put_usage_timeout(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    mock_http_session.put.side_effect = requests.ConnectTimeout()

    # WHEN
    with pytest.raises(MeteringServiceClientError):
        client.put_usage(MOCK_IDENTITY, "op", MOCK_USAGE)


def test_get_throttling(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    mock_response = GetThrottlingResponse(throttled=False)
    mock_http_response = mock.Mock()
    mock_http_response.status_code = 200
    mock_http_response.json.return_value = mock_response.dict(exclude_unset=True)
    mock_http_session.get.return_value = mock_http_response

    # WHEN
    response = client.get_throttling(MOCK_IDENTITY)

    # THEN
    assert response == mock_response


def test_get_throttling_unavailable(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    mock_http_response = mock.Mock()
    mock_http_response.status_code = 503
    mock_http_response.text.return_value = "service unavailable"
    mock_http_session.get.return_value = mock_http_response

    # WHEN
    with pytest.raises(MeteringServiceHTTPError) as e:
        client.get_throttling(MOCK_IDENTITY)

    # THEN
    assert e.value.http_status == 503


def test_get_throttling_retry_failure(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    client._retry_config = RetryConfig(
        max_attempts=3,
        multiplier=0.0,
        http_statuses=(503,),
    )
    mock_http_response = mock.Mock()
    mock_http_response.status_code = 503
    mock_http_response.text.return_value = "service unavailable"
    mock_http_session.get.return_value = mock_http_response

    # WHEN
    with pytest.raises(MeteringServiceHTTPError) as e:
        client.get_throttling(MOCK_IDENTITY)

    # THEN
    assert e.value.http_status == 503
    assert mock_http_session.get.call_count == 3


def test_get_throttling_retry_success(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    client._retry_config = RetryConfig(
        max_attempts=3,
        multiplier=0.0,
        http_statuses=(503,),
    )
    mock_503_response = mock.Mock()
    mock_503_response.status_code = 503
    mock_503_response.text.return_value = "service unavailable"

    mock_200_response = mock.Mock()
    mock_200_response.status_code = 200
    mock_200_response.json.return_value = GetThrottlingResponse(throttled=False).dict(exclude_unset=True)
    mock_http_session.get.side_effect = [
        mock_503_response,
        mock_200_response,
    ]

    # WHEN
    response = client.get_throttling(MOCK_IDENTITY)

    # THEN
    # no exception
    assert not response.throttled
    assert mock_http_session.get.call_count == 2


def test_get_throttling_retry_on_cause_exception(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    client._retry_config = RetryConfig(
        max_attempts=3,
        multiplier=0.0,
        cause_exception_types=(requests.ConnectTimeout,),
    )

    mock_http_session.get.side_effect = requests.ConnectTimeout()

    # WHEN
    with pytest.raises(MeteringServiceClientError):
        client.get_throttling(MOCK_IDENTITY)

    # THEN
    assert mock_http_session.get.call_count == 3


def test_get_throttling_retry_on_exception(mock_http_session, client: SyncMeteringServiceClient):
    # GIVEN
    client._retry_config = RetryConfig(
        max_attempts=3,
        multiplier=0.0,
        exception_types=(MeteringServiceClientError,),
    )

    mock_http_session.get.side_effect = requests.ConnectTimeout()

    # WHEN
    with pytest.raises(MeteringServiceClientError):
        client.get_throttling(MOCK_IDENTITY)

    # THEN
    assert mock_http_session.get.call_count == 3
