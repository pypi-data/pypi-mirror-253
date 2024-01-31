# Buildgrid Metering Service Client

🚧 This library is currently WIP and the interfaces might not be stable while the version below `1.0.0`. 🚧

Asyncio Python client of [`buildgrid-metering`](https://gitlab.com/BuildGrid/buildgrid-metering) service.

## Example

Suppose `buildgrid-metering` is running on `http://localhost:8000` requiring no authentication.
The service can be queried using this library via its `asyncio` interfaces.

```python
import asyncio
from buildgrid_metering.client import MeteringServiceClient
from buildgrid_metering.client.auth import (
    AuthTokenConfig,
    AuthTokenLoader,
    AuthTokenMode,
)
from buildgrid_metering.models.dataclasses import ComputingUsage, Identity, Usage

token_loader = AuthTokenLoader(AuthTokenConfig(AuthTokenMode.NONE, ""))
client = MeteringServiceClient("http://localhost:8000", token_loader)
identity = Identity(instance="dev", workflow="build", actor="tool", subject="username")


async def main():
    # Put usage of identity
    usage = Usage(computing=ComputingUsage(utime=1, stime=2, maxrss=3))
    await client.put_usage(identity, "op", usage)

    # Check throttling of identity
    resp = await client.get_throttling(identity)
    print(resp)


if __name__ == "__main__":\
    # Run the script with asyncio
    asyncio.run(main())

```

## Contact us

See more details at [BuildGrid Resources](https://buildgrid.build/user/about.html#resources).

## Contributing

See more details at [CONTRIBUTING.md](./CONTRIBUTING.md) and [BuildGrid](https://buildgrid.build/developer/contributing.html).
