import logging
from typing import Any, Dict

from aiohttp import ClientSession

_LOGGER = logging.getLogger(__name__)


class API:
    _http_base_url: str
    _token: str

    def __init__(
        self,
        host: str,
        token: str,
        scheme: str = "https",
        port: int = 8443,
        version: str = "v1"
    ) -> None:
        self._http_base_url = f"{scheme}://{host}:{port}/{version}"
        self._token = token

    async def get(self, path: str) -> Any:
        url = f"{self._http_base_url}{path}"
        _LOGGER.debug("Making GET request to %s", url)
        client_session = ClientSession()
        try:
            async with client_session.get(
                url,
                headers=self._headers(),
                ssl=False,
                timeout=30
            ) as res:
                res.raise_for_status()
                return await res.json()
        finally:
            await client_session.close()

    async def patch(self, path: str, json: Dict) -> None:
        url = f"{self._http_base_url}{path}"
        _LOGGER.debug("Making GET request to %s", url)
        client_session = ClientSession()
        try:
            async with client_session.patch(
                url,
                json=json,
                headers=self._headers(),
                ssl=False,
                timeout=30
            ) as res:
                res.raise_for_status()
        finally:
            await client_session.close()

    def _headers(self) -> Dict[str, Any]:
        return {"Authorization": f"Bearer {self._token}"}
