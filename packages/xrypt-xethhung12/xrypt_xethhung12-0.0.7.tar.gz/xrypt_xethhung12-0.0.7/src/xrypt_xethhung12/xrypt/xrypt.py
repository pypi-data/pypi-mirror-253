import base64
import json
from dataclasses import dataclass

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.types import PublicKeyTypes, PrivateKeyTypes


def read_public_key_from_pem(file_path) -> PublicKeyTypes:
    with open(file_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key


def read_private_key_from_pem(file_path, password=None) -> PrivateKeyTypes:
    with open(file_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=password)
    return private_key


class DeEnCryptor:
    def __init__(self, public_key: PublicKeyTypes, private_key: PrivateKeyTypes):
        self.public_key = public_key
        self.private_key = private_key

    def encryptToContainer(self, r_pub: PublicKeyTypes, data: str) -> 'DataContainer':
        data = data.encode('utf-8')
        signature = self.private_key.sign(data, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
        signature = base64.b64encode(signature).decode('ascii')
        iv = Random.new().read(AES.block_size)
        enIv = base64.b64encode(iv)
        enIv = r_pub.encrypt(enIv, padding=padding.PKCS1v15())
        enIv = base64.b64encode(enIv).decode('ascii')

        key = Random.new().read(32)
        enKey = base64.b64encode(key)
        enKey = r_pub.encrypt(enKey, padding=padding.PKCS1v15())
        enKey = base64.b64encode(enKey).decode('ascii')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # data = base64.b64encode(data)
        cipher_text = pad(data, AES.block_size)
        cipher_text = cipher.encrypt(cipher_text)
        cipher_text = base64.b64encode(cipher_text).decode('ascii')

        return DataContainer(data=cipher_text, iv=enIv, key=enKey, sign=signature)

    def encryptToJsonContainer(self, public_key: PublicKeyTypes, data: str) -> str:
        return json.dumps(self.encryptToContainer(public_key, data).to_dict())

    def decryptContainer(self, public_key: PublicKeyTypes, container: 'DataContainer') -> str:
        data = base64.b64decode(container.data)
        keyBytes = base64.b64decode(container.key.encode("ascii"))
        keyBytes = self.private_key.decrypt(keyBytes, padding.PKCS1v15())
        keyBytes = base64.b64decode(keyBytes)

        ivBytes = base64.b64decode(container.iv.encode("ascii"))
        ivBytes = self.private_key.decrypt(ivBytes, padding.PKCS1v15())
        ivBytes = base64.b64decode(ivBytes)

        cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)
        decrypted = cipher.decrypt(data)
        decrypted = unpad(decrypted, 16)

        sign = base64.b64decode(container.sign.encode("ascii"))
        public_key.verify(sign, decrypted, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
        return decrypted.decode("utf-8")


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
