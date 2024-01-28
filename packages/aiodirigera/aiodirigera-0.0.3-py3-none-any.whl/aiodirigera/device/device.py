from __future__ import annotations

import logging
from typing import Dict, TYPE_CHECKING


if TYPE_CHECKING:
    from aiodirigera.api_model import DeviceStatus
    from aiodirigera.hub import Hub

_LOGGER = logging.getLogger(__name__)


class Device:
    _hub: Hub
    _status: DeviceStatus

    def __init__(self, hub: Hub, status: DeviceStatus) -> None:
        self._hub = hub
        self._status = status

    @property
    def id(self) -> str:
        _LOGGER.info("_status is %s", self._status)
        return self._status.id

    @property
    def name(self) -> str:
        return self._status.attributes.customName

    @property
    def manufacturer(self) -> str:
        return self._status.attributes.manufacturer

    @property
    def model(self) -> str:
        return self._status.attributes.model

    @property
    def serial_number(self) -> str:
        return self._status.attributes.serialNumber

    @property
    def firmware_version(self) -> str:
        return self._status.attributes.firmwareVersion

    async def update_state(self) -> None:
        self._status = await self._hub.get_device_status(self.id)
        _LOGGER.info("Updated _status to %s", self._status)

    async def _update_device(self, data: Dict) -> None:
        await self._hub.update_device(self.id, data)


class OnOffDevice(Device):

    @property
    def is_on(self) -> bool:
        return self._status.attributes.isOn

    async def turn_on(self) -> None:
        await self._update_device([{"attributes": {"isOn": True}}])

    async def turn_off(self) -> None:
        await self._update_device([{"attributes": {"isOn": False}}])
