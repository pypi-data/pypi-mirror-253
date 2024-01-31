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


from typing import Optional

from pydantic import BaseModel, Field

from buildgrid_metering.models.dataclasses import Usage


class GetThrottlingResponse(BaseModel):
    """Summary if an identity should be throttled for the next remote execution

    Args:
        throttled (bool): if an identity should be throttled for the next remote execution
        tracked_usage (Usage): A subset of resource usage that is over the threshold
        tracked_time_window_secs: If set, this is the time window in seconds
            when the identity over consumed resource usage
    """

    throttled: bool
    tracked_usage: Optional[Usage] = None
    tracked_time_window_secs: Optional[int] = None


class PutUsageRequest(BaseModel):
    """Put the resource usage of an identity

    Args:
        operation_name (str): REAPI operation name
        usage (Usage): resource usage
    """

    operation_name: str = Field(..., description="REAPI operation name")
    usage: Usage = Field(..., description="Resource usage associated with the operation")
