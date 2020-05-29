from src.functions.func import *
from pathlib import Path
import numpy as np


def calculate_online_cpa(traces, num_traces, hyp, num_point, sub_key, k_guess):
    [num_sum_1, num_sum_2, num_sum_3,
     den_sum_1, den_sum_2, den_sum_3, den_sum_4] = to_zero(7, num_point)

    data_saving = np.array([])
    data_to_use = np.array([])

    beginning = 0

    div = num_traces / CPA_N

    if div != 1.0:
        prev_trace = num_traces - CPA_N
        file_name = ONLINE_CPA_EXE + SUB_KEY_STR + str(sub_key) \
                    + JOIN + \
                    NUM_TRACES_STR + str(prev_trace) + '.npy'

        data_file = Path(file_name)
        if data_file.is_file():
            data_to_use = read_np([file_name])  # Read data
            beginning = prev_trace  # Change the starting number for the index

            num_sum_2 = data_to_use[0][k_guess][0:int(NP_SIZE * 0.25)]
            num_sum_3 = data_to_use[0][k_guess][int(NP_SIZE * 0.25):int(NP_SIZE * 0.5)]
            den_sum_2 = data_to_use[0][k_guess][int(NP_SIZE * 0.5):int(NP_SIZE * 0.75)]
            den_sum_4 = data_to_use[0][k_guess][int(NP_SIZE * 0.75):int(NP_SIZE)]


        else:
            print("ERROR: No file for reading the data.")
            return -1

    for trace_i in range(0, beginning):
        h_i = hyp[trace_i]  # Set it as a variable to ease the reading
        t_i = traces[trace_i, :]

        # Numerator
        num_sum_1 = num_sum_1 + (h_i * t_i)

        # Left part of the Denominator
        den_sum_1 = den_sum_1 + h_i

        # Right part of the Denominator
        den_sum_3 = den_sum_3 + t_i

    # The formula is calculated for all the traces because of the sum -> N
    for trace_i in range(beginning, num_traces - 1):
        h_i = hyp[trace_i]  # Set it as a variable to ease the reading
        t_i = traces[trace_i, :]

        # Numerator
        num_sum_1 = num_sum_1 + (h_i * t_i)

        num_sum_2 = num_sum_2 + h_i
        num_sum_3 = num_sum_3 + t_i

        # Left part of the Denominator
        den_sum_1 = den_sum_1 + h_i
        den_sum_2 = den_sum_2 + (h_i * h_i)

        # Right part of the Denominator
        den_sum_3 = den_sum_3 + t_i
        den_sum_4 = den_sum_4 + t_i * t_i

    # Loop saving the data
    for trace_i in range(num_traces - 1, num_traces):
        h_i = hyp[trace_i]  # Set it as a variable to ease the reading
        t_i = traces[trace_i, :]

        # Numerator
        num_sum_1 = num_sum_1 + (h_i * t_i)
        num_sum_2 = num_sum_2 + h_i
        num_sum_3 = num_sum_3 + t_i

        data_saving = np.concatenate([data_saving, num_sum_2], axis=0)  # Sum of h the first element
        data_saving = np.concatenate([data_saving, num_sum_3])  # Sum of m the second element

        # Left part of the Denominator
        den_sum_1 = den_sum_1 + h_i
        den_sum_2 = den_sum_2 + (h_i * h_i)

        # print(den_sum_2)

        data_saving = np.concatenate([data_saving, den_sum_2])  # Sum of the square of h the third element

        # Right part of the Denominator
        den_sum_3 = den_sum_3 + t_i
        den_sum_4 = den_sum_4 + t_i * t_i
        data_saving = np.concatenate([data_saving, den_sum_4])  # Sum of the square of m the forth element

    # Numerator
    num_result = (num_traces * num_sum_1) - (num_sum_2 * num_sum_3)  # Result of the numerator

    # Left part of the Denominator
    den_sum_1 = den_sum_1 * den_sum_1  # Square the first sum of the denominator
    left_den = den_sum_1 - num_traces * den_sum_2  # Calculate left part of the denominator

    # Right part of the Denominator
    den_sum_3 = den_sum_3 * den_sum_3
    right_den = den_sum_3 - num_traces * den_sum_4

    return num_result / np.sqrt(left_den * right_den), data_saving  # Calculate the output online cpa value


def calculate_cpa(traces, num_traces, hyp, h_mean, t_mean, num_point):
    # Set to zeros according to the total number of traces -> N
    [sum_num, sum_den_1, sum_den_2] = to_zero(3, num_point)

    # The formula is calculated for all the traces because of the sum -> N
    for trace_i in range(0, num_traces):  # TODO Now this is set to less
        h_diff = (hyp[trace_i] - h_mean)  # Difference of hypothesis value
        t_diff = traces[trace_i, :] - t_mean  # Difference of traces value

        sum_num = sum_num + (h_diff * t_diff)  # Sum of the numerator
        sum_den_1 = sum_den_1 + h_diff * h_diff  # Left Sum of the denominator
        sum_den_2 = sum_den_2 + t_diff * t_diff  # Right Sum of the denominator

    return sum_num / np.sqrt(sum_den_1 * sum_den_2)  # Calculate the output cpa value


# Go through all the different hypothesis
def check_sub_key(num_point, num_traces, plain_txt, sub_key, HW, traces, cpa_output, max_cpa, is_online):
    """
    Performs all the execution for a sub-key
    """
    # Go through all the different hypothesis
    if is_online:
        data_saving = to_zero(1, 20000)

    for k_guess in range(0, 10):

        # print("Subkey %2d, hyp = %02x: " % (sub_key, k_guess)),

        hyp = np.zeros(num_traces)  # Set to zeros

        # Get the hypothesis for the trace
        for trace_i in range(0, num_traces):
            sbox_output = intermediate(plain_txt[trace_i][sub_key], k_guess)  # Get the sbox output
            hyp[trace_i] = HW[sbox_output]  # Get the amount of 1s of the integer from the output of the sbox

        h_mean = np.mean(hyp, dtype=np.float64)  # Mean of hypothesis
        t_mean = np.mean(traces, axis=0, dtype=np.float64)  # Mean of all points in trace

        # For each trace calculate the formula
        if is_online:
            cpa_output[k_guess], aux_data_saving = calculate_online_cpa(
                traces, num_traces, hyp, num_point, sub_key, k_guess)

            data_saving = np.vstack((data_saving, aux_data_saving))  # Save the new data received
        else:
            cpa_output[k_guess] = calculate_cpa(traces, num_traces, hyp, h_mean, t_mean, num_point)

        max_cpa[k_guess] = max(abs(cpa_output[k_guess]))

    if is_online:
        data_saving = np.delete(data_saving, 0, axis=0)  # Remove first row of 0s
        save_data(sub_key, num_traces, data_saving)

    # print(max_cpa[k_guess])
    return max_cpa


def cpa(input_num_traces, input_sub_key_amount, is_online):
    if is_online is True:
        print("Online CPA Execution: Traces:{} \tSub key:{}".format(input_num_traces, input_sub_key_amount))
        save_folder = ONLINE_CPA_FOLDER

        if not input_num_traces / CPA_N >= 1 or not input_num_traces % CPA_N == 0:
            print("Incorrect number of traces for online CPA, check CPA_N in constants.py")
            return -1
    else:
        print("CPA Execution: Traces:{} \tSub key:{}".format(input_num_traces, input_sub_key_amount))
        save_folder = CPA_FOLDER

    # Define the HW variable - Count the number of 1s in each number [0,SIZE]
    HW = [bin(n).count("1") for n in range(0, SIZE)]

    # Read data from .npy files
    [traces, plain_txt, known_key] = read_np([CHIP_FOLDER + TRACES, CHIP_FOLDER + PLAIN, CHIP_FOLDER + KEY])

    # Getting the amount of traces and points
    num_traces = np.shape(traces)[0] - 1  # -> N measurements
    num_point = np.shape(traces)[1]  # -> z data points

    # Use less than the maximum traces by setting num_traces to something  # TODO
    num_traces = input_num_traces  # Set for Testing purposes -> N measurements

    # Set 16 to something lower (like 1) to only go through a single sub-key  # TODO
    best_guess = [0] * input_sub_key_amount  # Set to zeros
    ge = np.zeros(input_sub_key_amount)

    for sub_key in range(0, input_sub_key_amount):  # Set just for the first sub-key
        cpa_output = [0] * SIZE  # Each entry for each different hypothesis
        max_cpa = [0] * SIZE  # To zero

        # Go through all the different hypothesis

        max_cpa = check_sub_key(num_point, num_traces, plain_txt, sub_key, HW, traces, cpa_output, max_cpa, is_online)

        # Get the best guess
        best_guess[sub_key] = np.argmax(max_cpa)

        # Sort max_cpa
        cpa_refs = np.argsort(max_cpa)[::-1]

        # Find GE accessing to the known key
        ge[sub_key] = list(cpa_refs).index(known_key[0][sub_key])  # TODO I don't know why that 0

    print_result(best_guess, ge)
    save_result(save_folder, best_guess, ge, input_sub_key_amount, num_traces)

    return 0
