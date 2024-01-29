import logging
from typing import Dict, List

from aiodirigera.api import API
from aiodirigera.api_model import HubStatus, DeviceStatus
from aiodirigera.device import Device, Light, EnvironmentSensor

_LOGGER = logging.getLogger(__name__)


class Hub:
    _delegate: API

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

    async def get_status(self) -> HubStatus:
        raw = await self._delegate.get("/hub/status")
        return HubStatus(**raw)

    async def get_device_statuses(self) -> List[DeviceStatus]:
        raw = await self._delegate.get("/devices")
        return [DeviceStatus(**x) for x in raw]

    async def get_devices(self) -> List[Device]:
        device_statuses = await self.get_device_statuses()
        return [
            self._build_device(device_status)
            for device_status in device_statuses
        ]

    async def get_device_status(self, id: str) -> DeviceStatus:
        raw = await self._delegate.get(f"/devices/{id}")
        return DeviceStatus(**raw)

    async def get_device(self, id: str) -> DeviceStatus:
        device_status = await self.get_device_status(id)
        return self._build_device(device_status)

    async def update_device(self, id: str, data: Dict) -> None:
        await self._delegate.patch(f"/devices/{id}", data)

    def _build_device(self, device_status: DeviceStatus) -> Device:
        device_type = device_status.deviceType
        if device_type == "light":
            return Light(self, device_status)
        elif device_type == "environmentSensor":
            return EnvironmentSensor(self, device_status)
        else:
            _LOGGER.warn("Unknown deviceType %s", device_type)
