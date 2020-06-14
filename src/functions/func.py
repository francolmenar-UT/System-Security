import os

import numpy as np

from src.constant.constant import SUB_KEY_STR, JOIN, NUM_TRACES_STR


def create_folder(folder):
    """
    Checks if a folder exists, if it does not it creates it
    :param folder: Folder to be created
    :return:
    """
    # Check if the folder does not exists
    if not os.path.isdir(folder):
        os.makedirs(folder)  # Create folder


def save_time(file, data_list, length):
    output_f = open(file, "w+")  # Open the output file
    data_str = ""

    # Save time against length
    for data in data_list:
        data_str += str(length) + ',' + str(data) + '\n'  # Append the data in a csv form

    output_f.write(data_str)  # Write the processed line to the output text file
    output_f.close()


def print_result(best_guess, ge, sub_key_amount):
    # Print result
    for b in range(0, sub_key_amount):
        print("Best Key Guess: ", best_guess[b], " GE: ", ge[b])


def read_np(files):
    result = []
    for file in files:
        result.append(np.load(r'' + file))
    return result


def to_zero(index, length):
    result = []
    for i in range(0, index):
        result.append(np.zeros(length))
    return result


def save_result(folder, best_guess, ge, sub_key_amount, num_traces):
    data = np.array([best_guess, ge])  # Create np array
    np.save(folder + SUB_KEY_STR + str(sub_key_amount)  # Save the data into file
            + JOIN +
            NUM_TRACES_STR + str(num_traces) + '.npy', data)
