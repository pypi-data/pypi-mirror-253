from typing import Optional

from aiodirigera.device import Device


class EnvironmentSensor(Device):
    temperature: Optional[int] = None
    humidity: Optional[int] = None

    async def update_state(self) -> None:
        device_status = await self._hub.get_device(self._id)

        self.name = device_status.attributes.customName
        self.manufacturer = device_status.attributes.manufacturer
        self.model = device_status.attributes.model
        self.serial_number = device_status.attributes.serialNumber
        self.firmware_version = device_status.attributes.firmwareVersion
        self.temperature = device_status.attributes.currentTemperature
        self.humidity = device_status.attributes.currentRH
