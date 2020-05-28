import timeit

from src.constants.constants import EXE_REP, MULT_ALW_FOLDER_PATH, MULT_ALW_FILE_PATH


def square_mult_alw(key_list):
    new_key_list = []
    for key in key_list:
        # Encryption
        enc_time = run(key.msg, key.e, key.n)

        new_key_list.append(key.add_time(enc_time))  # Add new KeyObject with time
    save_results(new_key_list)
    return new_key_list


def run(msg, exponent, n):
    enc_time = timeit.timeit(lambda: exp(msg, exponent, n), number=EXE_REP)
    return enc_time


def exp(m, e, n):
    # Assigning initial values
    R0 = 1
    R1 = m
    c = '{0:b}'.format(e)
    i = len(c) - 1
    t = 0
    c = c[::-1]

    while i >= 0:
        if t == 0:
            Rt = R0
        elif t == 1:
            Rt = R1
        # Operations
        R0 = (R0 * Rt) % n
        d = int(c[i])  # Get the bit
        t = (t ^ d)  # XOR
        i = i - 1 + t  # Adjust counter
    return R0


def save_results(key_list):
    """
    Saves a list of KeyObject into a csv filed defined in the constants file
    :param key_list: List of KeyObject
    :return: 0 in success
    """
    output_f = open(MULT_ALW_FOLDER_PATH + MULT_ALW_FILE_PATH, "w+")  # Open the output file
    keys_str = ""

    for key in key_list:
        keys_str += str(key.e) + ',' + str(key.enc_time) + '\n'  # Append the data in a csv form

    output_f.write(keys_str)  # Write the processed line to the output text file
    return 0
