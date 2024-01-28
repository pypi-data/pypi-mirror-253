# Copied and modified from Leggin/dirigera under MIT License

import string
import hashlib
import random
import socket
import base64

from aiohttp import ClientSession

ALPHABET = f"_-~.{string.ascii_letters}{string.digits}"
CODE_LENGTH = 128


def random_char(alphabet: str) -> str:
    return alphabet[random.randrange(0, len(alphabet))]


def random_code(alphabet: str, length: int) -> str:
    return "".join([random_char(alphabet) for _ in range(0, length)])


def code_challenge(code_verifier: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(code_verifier.encode())
    digest = sha256_hash.digest()
    sha256_hash_as_base64 = (
        base64.urlsafe_b64encode(digest).rstrip(b"=").decode("us-ascii")
    )
    return sha256_hash_as_base64


async def send_challenge(
    ip_address: str,
    code_verifier: str,
    client_session: ClientSession = ClientSession()
) -> str:
    url = f"https://{ip_address}:8443/v1/oauth/authorize"
    params = {
        "audience": "homesmart.local",
        "response_type": "code",
        "code_challenge": code_challenge(code_verifier),
        "code_challenge_method": "S256",
    }

    try:
        async with client_session.get(
            url,
            params=params,
            ssl=False,
            timeout=30
        ) as res:
            res.raise_for_status()
            res_json = await res.json()
            return res_json["code"]
    finally:
        await client_session.close()


async def get_token(
    ip_address: str,
    code: str,
    code_verifier: str,
    client_session: ClientSession = ClientSession()
) -> str:
    url = f"https://{ip_address}:8443/v1/oauth/token"
    data = str(
        "code="
        + code
        + "&name="
        + socket.gethostname()
        + "&grant_type="
        + "authorization_code"
        + "&code_verifier="
        + code_verifier
    )
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        async with client_session.post(
            url,
            data=data,
            headers=headers,
            ssl=False,
            timeout=30
        ) as res:
            res.raise_for_status()
            res_json = await res.json()
            return res_json["access_token"]
    finally:
        await client_session.close()
