from .device import OnOffDevice


class Light(OnOffDevice):

    @property
    def brightness(self) -> int:
        return self._status.attributes.lightLevel

    async def set_brightness(self, brightness: int) -> None:
        if brightness < 1 or brightness > 100:
            raise ValueError("Brightness must be in range [1, 100]")

        await self._update_device([{"attributes": {"lightLevel": brightness}}])
