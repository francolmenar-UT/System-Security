from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from src.key_object import KeyObject


def create_key(e, key_s):
    key = rsa.generate_private_key(
        public_exponent=e,
        key_size=key_s,
        backend=default_backend()
    )
    return KeyObject(key=key, key_size=key_s)
