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


class MeteringServiceError(RuntimeError):
    """Base class of all errors"""


class MeteringServiceHTTPError(MeteringServiceError):
    """Errors indicated by the HTTP status, e.g., 400, 503"""

    http_status: int
    message: str

    def __init__(self, http_status: int, message: str) -> None:
        super().__init__(http_status, message)
        self.http_status = http_status
        self.message = message


class MeteringServiceClientError(MeteringServiceError):
    """Client connection errors, e.g. timeout, connection closed"""

    message: str

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
