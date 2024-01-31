import base64
import json
from dataclasses import dataclass
from typing import Optional

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.types import PublicKeyTypes, PrivateKeyTypes


class Signer:
    def __init__(self, private_key: PrivateKeyTypes):
        self.private_key = private_key

    def sign(self, data: str) -> 'SignedData':
        raw_data = data
        data = data.encode('utf-8')
        signature = self.private_key.sign(data, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
        signature = base64.b64encode(signature).decode('ascii')
        return SignedData(signature, raw_data)


class Verifier:
    def __init__(self, public_key: PublicKeyTypes):
        self.public_key = public_key

    def verify(self, signed_data: 'SignedData') -> bool:
        try:
            self.public_key.verify(base64.b64decode(signed_data.signature.encode('ascii')),
                                   signed_data.data.encode('utf-8'), padding=padding.PKCS1v15(),
                                   algorithm=hashes.SHA256())
            return True
        except Exception:
            return False


class DeEnCryptor:
    def __init__(self, public_key: PublicKeyTypes, private_key: PrivateKeyTypes):
        self.public_key = public_key
        self.private_key = private_key

    def encryptToContainer(self, r_pub: PublicKeyTypes, data: str) -> 'DataContainer':
        signature = Signer(self.private_key).sign(data).signature
        data = data.encode('utf-8')
        # signature = self.private_key.sign(data, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
        # signature = base64.b64encode(signature).decode('ascii')
        iv = Random.new().read(AES.block_size)
        en_iv = base64.b64encode(iv)
        en_iv = r_pub.encrypt(en_iv, padding=padding.PKCS1v15())
        en_iv = base64.b64encode(en_iv).decode('ascii')

        key = Random.new().read(32)
        en_key = base64.b64encode(key)
        en_key = r_pub.encrypt(en_key, padding=padding.PKCS1v15())
        en_key = base64.b64encode(en_key).decode('ascii')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher_text = pad(data, AES.block_size)
        cipher_text = cipher.encrypt(cipher_text)
        cipher_text = base64.b64encode(cipher_text).decode('ascii')

        return DataContainer(data=cipher_text, iv=en_iv, key=en_key, sign=signature)

    def encryptToJsonContainer(self, public_key: PublicKeyTypes, data: str, indent: int = None) -> str:
        return json.dumps(self.encryptToContainer(public_key, data).to_dict(), indent=indent)

    def decryptContainer(self, public_key: PublicKeyTypes, container: 'DataContainer') -> Optional[str]:
        data = base64.b64decode(container.data)
        key_bytes = base64.b64decode(container.key.encode("ascii"))
        key_bytes = self.private_key.decrypt(key_bytes, padding.PKCS1v15())
        key_bytes = base64.b64decode(key_bytes)

        iv_bytes = base64.b64decode(container.iv.encode("ascii"))
        iv_bytes = self.private_key.decrypt(iv_bytes, padding.PKCS1v15())
        iv_bytes = base64.b64decode(iv_bytes)

        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        decrypted = cipher.decrypt(data)
        decrypted = unpad(decrypted, 16)

        if Verifier(public_key).verify(SignedData(container.sign, decrypted.decode("utf-8"))):
            return decrypted.decode("utf-8")
        else:
            return None


@dataclass
class DataContainer:
    sign: str
    iv: str
    key: str
    data: str

    @staticmethod
    def from_json(d: dict) -> 'DataContainer':
        return DataContainer(d['sign'], d['iv'], d['key'], d['data'])

    def to_dict(self) -> dict:
        return {'sign': self.sign, 'iv': self.iv, 'key': self.key, 'data': self.data}


@dataclass
class SignedData:
    signature: str
    data: str

    @staticmethod
    def from_json(d: dict) -> 'SignedData':
        return SignedData(d['signature'], d['data'])

    def to_dict(self) -> dict:
        return {'signature': self.signature, 'data': self.data}
