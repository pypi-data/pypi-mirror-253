from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.types import PrivateKeyTypes, PublicKeyTypes


def pri_key_to_pem(pri_key: PrivateKeyTypes) -> str:
    return pri_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    ).decode('utf-8')


def pub_key_to_pem(pub_key: PublicKeyTypes) -> str:
    return pub_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.PKCS1
    ).decode('utf-8')
