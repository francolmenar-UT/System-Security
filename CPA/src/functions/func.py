from src.constants.constants import *
import numpy as np


def intermediate(plain_txt, key_guess):
    return SBOX[plain_txt ^ key_guess]


def print_result(best_guess, ge):
    # Print result
    for b in range(0, SUB_KEY_AMOUNT):
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


def save_data(sub_key_amount, num_traces, data):
    np.save(ONLINE_CPA_EXE + SUB_KEY_STR + str(sub_key_amount)  # Save the data into file
            + JOIN +
            NUM_TRACES_STR + str(num_traces) + '.npy', data)


def save_time(data_list, is_online):
    if is_online:
        folder = ONLINE_CPA_TIMING
        file = ONLINE_PREFIX
    else:
        folder = CPA_TIMING
        file = CPA_PREFIX

    output_f = open(folder + file + ".csv", "w+")  # Open the output file
    data_str = ""

    # Save time against sub-key with defined traces max
    for data in data_list:
        for idx, atr in enumerate(data):
            if idx == SUB_KEY_INDEX:
                data_str += str(atr) + ','  # Append the data in a csv form
            elif idx == EXE_TIME_INDEX:
                data_str += str(atr)  # Append the data in a csv form
        data_str += '\n'

    output_f.write(data_str)  # Write the processed line to the output text file
    output_f.close()

    # Save sub-key against ge
    if is_online:
        folder = ONLINE_CPA_GE
        file = ONLINE_PREFIX
    else:
        folder = CPA_GE
        file = CPA_PREFIX

    output_f = open(folder + file + ".csv", "w+")  # Open the output file
    data_str = ""

    for data in data_list:
        for idx, atr in enumerate(data):
            if idx == SUB_KEY_INDEX:
                data_str += str(atr) + ','  # Append the data in a csv form
            elif idx == GE_INDEX:
                data_str += str(atr[int(atr[SUB_KEY_INDEX]) - 1])  # Append the data in a csv form
        data_str += '\n'

    output_f.write(data_str)  # Write the processed line to the output text file
    output_f.close()

    return 0
