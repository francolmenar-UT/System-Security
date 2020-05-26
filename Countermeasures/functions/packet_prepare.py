from constants.constants import keys_path
from functions.crypto import rsa_encrypt


def create_message(message):
    # Create array of keys
    key_file = open(keys_path, "rb")
    pub_key = key_file.read()
    key_file.close()

    encrypted_message = rsa_encrypt(message, pub_key)

    return encrypted_message
