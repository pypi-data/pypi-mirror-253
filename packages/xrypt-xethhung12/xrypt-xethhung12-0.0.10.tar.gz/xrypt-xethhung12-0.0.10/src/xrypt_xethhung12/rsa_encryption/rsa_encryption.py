from cryptography.hazmat.backends import default_backend as crypto_default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.types import PublicKeyTypes, PrivateKeyTypes


def gen_key_pair(key_size: int = 8192) -> (PublicKeyTypes, PrivateKeyTypes):
    pri_key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=key_size
    )
    return pri_key.public_key(), pri_key


def read_public_key_from_pem_str(pub_key_str: str) -> PublicKeyTypes:
    return serialization.load_pem_public_key(pub_key_str.encode('ascii'))


def read_private_key_from_pem_str(pri_key_str: str, password=None) -> PrivateKeyTypes:
    return serialization.load_pem_private_key(pri_key_str.encode('ascii'), password)


def read_public_key_from_pem(file_path) -> PublicKeyTypes:
    with open(file_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key


def read_private_key_from_pem(file_path, password=None) -> PrivateKeyTypes:
    with open(file_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=password)
    return private_key
