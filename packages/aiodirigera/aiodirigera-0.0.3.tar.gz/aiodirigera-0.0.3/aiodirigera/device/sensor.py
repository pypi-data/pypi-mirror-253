from .device import Device


class EnvironmentSensor(Device):

    @property
    def temperature(self) -> int:
        return self._status.attributes.currentTemperature

    @property
    def humidity(self) -> int:
        return self._status.attributes.currentRH
