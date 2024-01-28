from typing import Optional

from aiodirigera.device import OnOffDevice


class Light(OnOffDevice):
    brightness: Optional[int] = None

    async def update_state(self) -> None:
        device_status = await self._hub.get_device(self._id)

        self.name = device_status.attributes.customName
        self.manufacturer = device_status.attributes.manufacturer
        self.model = device_status.attributes.model
        self.serial_number = device_status.attributes.serialNumber
        self.firmware_version = device_status.attributes.firmwareVersion
        self.is_on = device_status.attributes.isOn
        self.brightness = device_status.attributes.lightLevel

    async def set_brightness(self, brightness: int) -> None:
        if brightness < 1 or brightness > 100:
            raise ValueError("Brightness must be in range [1, 100]")

        await self._hub.update_device(
            self._id,
            [{"attributes": {"lightLevel": brightness}}]
        )
