from typing import Dict, Optional

from aiodirigera.api_model import DeviceStatus
from aiodirigera.hub import Hub


class Device:
    _hub: Hub
    _id: str

    name: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    firmware_version: Optional[str] = None

    def __init__(self, hub: Hub, id: str) -> None:
        self._hub = hub
        self._id = id

    async def get_status(self) -> DeviceStatus:
        return await self._hub.get_device(self._id)

    async def update_status(self, data: Dict) -> None:
        await self._hub.update_device(self._id, data)


class OnOffDevice(Device):
    is_on: Optional[bool] = None

    async def turn_on(self) -> None:
        await self._hub.update_device(
            self._id,
            [{"attributes": {"isOn": True}}]
        )

    async def turn_off(self) -> None:
        await self._hub.update_device(
            self._id,
            [{"attributes": {"isOn": False}}]
        )
