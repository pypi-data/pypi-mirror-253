from typing import Dict, List

from aiodirigera.api import API
from aiodirigera.api_model import HubStatus, DeviceStatus


class Hub:
    _delegate: API = None

    def __init__(
        self,
        host: str,
        token: str,
        scheme: str = "https",
        port: int = 8443,
        version: str = "v1"
    ) -> None:
        self._delegate = API(
            host,
            token,
            scheme=scheme,
            port=port,
            version=version
        )

    async def get_hub_status(self) -> HubStatus:
        raw = await self._delegate.get("/hub/status")
        return HubStatus(**raw)

    async def get_devices(self) -> List[DeviceStatus]:
        raw = await self._delegate.get("/devices")
        return [DeviceStatus(**x) for x in raw]

    async def get_device(self, id: str) -> DeviceStatus:
        raw = await self._delegate.get(f"/devices/{id}")
        return DeviceStatus(**raw)

    async def update_device(self, id: str, data: Dict) -> None:
        await self._delegate.patch(f"/devices/{id}", data)
