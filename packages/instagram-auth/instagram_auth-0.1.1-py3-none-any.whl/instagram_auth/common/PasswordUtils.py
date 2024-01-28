__author__ = "Николай Витальевич Никоноров (Bitnik212)"
__date__ = "12.01.2024 06:45"

import base64
import binascii
import datetime
import struct

from Cryptodome import Random
from Cryptodome.Cipher import AES
from aiohttp import ClientSession

from nacl.public import PublicKey, SealedBox


class PasswordUtils:

    def __init__(self, session: ClientSession | None = None):
        self.session = session or ClientSession(raise_for_status=True)

    async def encrypt(self, password):
        """
        source: https://gist.github.com/lorenzodifuccia/c857afa47ede66db852e6a25c0a1a027
        """
        key_id, version, pub_key = await self.public_keys()
        key = Random.get_random_bytes(32)
        iv = bytes([0] * 12)

        time = int(datetime.datetime.now().timestamp())

        aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
        aes.update(str(time).encode('utf-8'))
        encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))

        pub_key_bytes = binascii.unhexlify(pub_key)
        seal_box = SealedBox(PublicKey(pub_key_bytes))
        encrypted_key = seal_box.encrypt(key)

        encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
        encrypted = base64.b64encode(encrypted).decode('utf-8')

        return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'

    async def public_keys(self) -> (int, int, str):
        url = "https://www.instagram.com/data/shared_data/"
        async with self.session as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data: dict = await response.json()
                    encryption: dict = data.get("encryption", {})
                    return int(encryption.get("key_id")), int(encryption.get("version")), encryption.get("public_key")
