import os
import datetime
import numpy as np
from src.constant.constant import SUB_KEY_STR, JOIN, NUM_TRACES_STR, DATA_CSV, CSV


def create_folder(folder):
    """
    Checks if a folder exists, if it does not it creates it
    :param folder: Folder to be created
    :return:
    """
    # Check if the folder does not exists
    if not os.path.isdir(folder):
        os.makedirs(folder)  # Create folder


def save_result_csv(result_i, profile_size, attack_size_i, noise):
    datetime.datetime.now().time()
    datetime.time(15, 8, 24, 78915)

    aux_time = datetime.datetime.now().time()
    file = DATA_CSV + "profile_size:" + str(profile_size) + "-attack_size:" + str(
        attack_size_i) + "-noise:" + str(noise) + "-time:" + str(aux_time) + CSV

    print(file)

    output_f = open(file, "w+")  # Open the output file
    data_str = ""

    # Save time against length
    for idx_1, array in enumerate(result_i):
        if isinstance(array, int):
            data_str += str(array)  # Append the data in a csv form

        else:
            for idx, val in enumerate(array):
                if idx == len(array) - 1:
                    data_str += str(val)
                else:
                    data_str += str(val) + "-"

        if idx_1 != len(result_i) - 1:
            data_str += ','  # Append the data in a csv form

    output_f.write(data_str)  # Write the processed line to the output text file
    output_f.close()


def print_result(best_guess, known_key, ge, comp_res, byte):
    # Print result
    print("Real  Key:{} , \t Best Key Guess: {}, \t Comp result: {} \t GE: {}".format(
        known_key[0][byte], best_guess, comp_res, ge))


def save_result(folder, best_guess, ge, sub_key_amount, num_traces):
    data = np.array([best_guess, ge])  # Create np array
    np.save(folder + SUB_KEY_STR + str(sub_key_amount)  # Save the data into file
            + JOIN +
            NUM_TRACES_STR + str(num_traces) + '.npy', data)
