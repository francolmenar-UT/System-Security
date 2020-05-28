import timeit

from src.constants.constants import EXE_REP, MULT_LD_FOLDER_PATH, MULT_LD_FILE_PATH


def square_ladder(key_list):
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
    enc_time = timeit.timeit(lambda: exp(msg, exponent, n), number=EXE_REP)
    return enc_time


def exp(m, e, n):
    """
    # TODO
    :param m:
    :param e:
    :param n:
    :return:
    """
    # Assigning initial values
    R0 = 1
    R1 = m
    c = '{0:b}'.format(e)
    i = len(c) - 1
    c = c[::-1]

    while i >= 0:
        d = int(c[i])  # Get the bit
        if d == 0:
            R1 = (R0 * R1) % n
            R0 = (R0 * R0) % n
        elif d == 1:
            R0 = (R0 * R1) % n
            R1 = (R1 * R1) % n
        i = i - 1
    return R0


def save_results(key_list):
    """
    Saves a list of KeyObject into a csv filed defined in the constants file
    :param key_list: List of KeyObject
    :return: 0 in success
    """
    output_f = open(MULT_LD_FOLDER_PATH + MULT_LD_FILE_PATH, "w+")  # Open the output file
    keys_str = ""

    for key in key_list:
        keys_str += str(key.e) + ',' + str(key.enc_time) + '\n'  # Append the data in a csv form

    output_f.write(keys_str)  # Write the processed line to the output text file
    return 0
