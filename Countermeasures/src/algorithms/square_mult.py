import time
import timeit

from src.constants.constants import MULT_FOLDER_PATH, MULT_FILE_PATH


def square_mult(key_list):
    """
    # TODO
    :param key_list:
    :return:
    """
    new_key_list = []
    for key in key_list:
        # Encryption
        enc_time = run(key.msg, key.e, key.n)

        new_key_list.append(key.add_time(enc_time))  # Add new KeyObject with time
    save_results(new_key_list)
    return new_key_list


def run(msg, exponent, n):
    """
    #TODO
    :param msg:
    :param exponent:
    :param n:
    :return:
    """
    enc_time = timeit.timeit(lambda: exp(msg, exponent, n), number=20)
    return enc_time


def exp(m, e, n):
    """
    Calculates the Square-and-Multiply Algorithm
    :param m: Base of the exponentiation
    :param e: Exponent
    :param n: Modulus
    :return: The result of the operation
    """
    m = m % n  # Calculate the modulus of the message at first
    d_bin = bin(e)  # Convert the exponent to bit string
    d_bin = d_bin[:0] + d_bin[0 + 2:]  # Remove first two characters to have the correct bit array

    result = 1

    for i in range(0, len(d_bin)):  # Travers the whole bit string
        result = (result * result) % n  # a <- a^2  mod n
        if d_bin[i:i + 1] == '1':  # If the bit is 1, the result is multiplied by the base
            result = (result * m) % n
    return result


def save_results(key_list):
    """
    Saves a list of KeyObject into a csv filed defined in the constants file
    :param key_list: List of KeyObject
    :return: 0 in success
    """
    output_f = open(MULT_FOLDER_PATH + MULT_FILE_PATH, "w+")  # Open the output file
    keys_str = ""

    for key in key_list:
        keys_str += str(key.e) + ',' + str(key.enc_time) + '\n'  # Append the data in a csv form

    output_f.write(keys_str)  # Write the processed line to the output text file
    return 0
