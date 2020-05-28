import numpy as np
import pandas as pd

from src.constants.constants import *
from src.objects.key_object import KeyObject


def generate_e():
    """
    Generates all the values for the exponent value according to the range values
    :return: Np array with the exponent values
    """
    x = np.arange(E[MIN], E[MAX], E_STEP)  # Create the array of exponents with the constant values defined
    index = []  # Array to remove the even elements

    for i, element in enumerate(x):
        if element % 2 == 0:  # Only odd exponents are valid
            index.append(i)
    return np.delete(x, index)  # Delete the elements which are not odd


def generate_rsa_keys(e_list):
    """
    Generates the RSA keys as a list of KeyObject
    :param e_list: List of exponents to be used
    :return: List with all the KeyObject created
    """
    key_list_aux = []
    for e_i in e_list:
        key_list_aux.append(KeyObject(e=e_i, n=N, msg=MSG))
    return key_list_aux


def save_keys(key_list):
    """
    Saves a list of KeyObject into a csv filed defined in the constants file
    :param key_list: List of KeyObject
    :return: 0 in success
    """
    output_f = open(KEY_FOLDER_PATH + KEY_FILE_PATH, "w+")  # Open the output file
    keys_str = ""

    for key in key_list:
        keys_str += str(key.e) + '\n'  # Append the data in a csv form

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
        key_list_loaded.append(KeyObject(e=int(row[0]), n=N, msg=MSG))  # Create the object with the csv data
    return key_list_loaded
