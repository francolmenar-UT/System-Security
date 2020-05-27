from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as padding_asymetric


def rsa_encrypt(msg, public_key_str):
    # Create the pub key object from the string
    public_key = serialization.load_pem_public_key(
        public_key_str,
        backend=default_backend())

    # Encrypt the message
    ciphertext = public_key.encrypt(
        msg,
        padding_asymetric.OAEP(
            mgf=padding_asymetric.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

    return ciphertext


def create_key():
    key = rsa.generate_private_key(
        public_exponent=3,
        key_size=512,
        backend=default_backend()
    )
    return key.public_key().public_numbers().e, key.private_numbers().d, key.public_key().public_numbers().n, key
