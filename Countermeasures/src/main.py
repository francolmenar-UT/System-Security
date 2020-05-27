from constants.constants import *
from functions.crypto import create_key
from src.key_object import KeyObject
from src.square_mult import square_mult
import numpy as np
import pandas as pd


def generate_keys(e, key_sz):
    key_list_aux = []
    for e_i in e:
        for k_i in key_sz:
            key_list_aux.append(create_key(np.int16(e_i).item(), np.int16(k_i).item()))
    return key_list_aux


def generate_key_size():
    """
    Generates all the values for the key size value according to the range values
    :return: Np array with the key size values
    """
    return np.arange(KEY_SIZE[MIN], KEY_SIZE[MAX], KEY_STEP)


def generate_e():
    """
    Generates all the values for the exponent value according to the range values
    :return: Np array with the exponent values
    """
    x = np.arange(E[MIN], E[MAX])
    index = []

    for i, element in enumerate(x):
        if element % 2 == 0:
            index.append(i)
    return np.delete(x, index)


def save_keys(keys):
    output_f = open("data.csv", "w+")  # Open the output file for the processed data
    keys_str = ""

    for key in keys:
        keys_str += str(key.e) + ',' + str(key.d) + ',' + str(key.n) + ',' + str(key.key_size) + '\n'

    output_f.write(keys_str)  # Write the processed line to the output text file
    return 0


def load_keys():
    key_list_loaded = []
    data = pd.read_csv('data.csv', header=None)
    for index, row in data.iterrows():
        key_list_loaded.append(KeyObject(e=int(row[0]), d=int(row[1]), n=int(row[2]), key_size=int(row[3])))
    return key_list_loaded


# e_list = generate_e()
# key_size = generate_key_size()

# key_list = generate_keys(e_list, key_size)
# print(key_list[0].e)
# save_keys(key_list)

key_list = load_keys()
key_list[0].toString()

# TODO Integrate the cli to operate better with it
# TODO Move the csv to data

# print(e)

# print("n: {}".format(n))
# print("e: {}".format(e))
# print("d: {}".format(d))
# print("msg: {}".format(msg))

# enc = square_mult(msg, e, n)

# print("enc: {}".format(enc))

# dec = square_mult(enc, d, n)

# print("dec: {}".format(dec))
