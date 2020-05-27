from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import numpy as np
import pandas as pd
from src.constants.constants import *

from src.objects.key_object import KeyObject


def generate_e():
    """
    Generates all the values for the exponent value according to the range values
    :return: Np array with the exponent values
    """
    x = np.arange(E[MIN], E[MAX])  # Create the array of exponents with the constant values defined
    index = []  # Array to remove the even elements

    for i, element in enumerate(x):
        if element % 2 == 0:  # Only odd exponents are valid
            index.append(i)
    return np.delete(x, index)  # Delete the elements which are not odd


def generate_key_size():
    """
    Generates all the values for the key size value according to the range values
    :return: Np array with the key size values
    """
    return np.arange(KEY_SIZE[MIN], KEY_SIZE[MAX], KEY_STEP)  # Creates a np array with the constant values


def generate_rsa_keys(e_list, key_sz_list):
    """
    Generates the RSA keys as a list of KeyObject
    :param e_list: List of exponents to be used
    :param key_sz_list: List of key sizes to be used
    :return: List with all the KeyObject created
    """
    key_list_aux = []
    for e_i in e_list:
        for k_i in key_sz_list:
            key_list_aux.append(create_key(np.int16(e_i).item(),  # Create and append the new key
                                           np.int16(k_i).item()))
    return key_list_aux


def create_key(e, key_s):
    """
    Creates an RSA key as a KeyObject
    :param e: Exponent to be used
    :param key_s: Key size to be used
    :return: A KeyObject as the newly created key
    """
    key = rsa.generate_private_key(
        public_exponent=e,
        key_size=key_s,
        backend=default_backend()
    )
    return KeyObject(key=key, key_size=key_s)


def save_keys(key_list):
    """
    Saves a list of KeyObject into a csv filed defined in the constants file
    :param key_list: List of KeyObject
    :return: 0 in success
    """
    output_f = open(KEY_FOLDER_PATH + KEY_FILE_PATH, "w+")  # Open the output file
    keys_str = ""

    for key in key_list:
        keys_str += str(key.e) + ',' + str(key.d) + ',' + \
                    str(key.n) + ',' + str(key.key_size) + '\n'  # Append the data in a csv form

    output_f.write(keys_str)  # Write the processed line to the output text file
    return 0


def load_keys():
    """
    Load the RSA keys from the defined csv file
    :return: A list of KeyObject with all the keys loaded
    """
    key_list_loaded = []
    data = pd.read_csv(KEY_FOLDER_PATH + KEY_FILE_PATH, header=None)  # Read the csv file
    for index, row in data.iterrows():  # Read each of the rows
        key_list_loaded.append(KeyObject(e=int(row[0]), d=int(row[1]),  # Create the object with the csv data
                                         n=int(row[2]), key_size=int(row[3])))
    return key_list_loaded
