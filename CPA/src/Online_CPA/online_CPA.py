from src.functions.CPA_func import *


def calculate_formula(traces, num_traces, hyp, h_mean, t_mean, sum_num, sum_den_1, sum_den_2, num_point):
    [num_sum_1, num_sum_2, num_sum_3,
     den_sum_1, den_sum_2, den_sum_3, den_sum_4] = to_zero(7, num_point)

    ####################################### New Formula  ######################################
    for trace_i in range(0, num_traces):
        # Numerator
        num_sum_1 = (num_sum_1 + (hyp[trace_i] * traces[trace_i, :]))
        num_sum_2 = (num_sum_2 + hyp[trace_i])
        num_sum_3 = (num_sum_3 + traces[trace_i, :])

        # Left part of the Denominator
        den_sum_1 = (den_sum_1 + hyp[trace_i])
        den_sum_2 = (den_sum_2 + (hyp[trace_i] * hyp[trace_i]))

        # Right part of the Denominator
        den_sum_3 = (den_sum_3 + traces[trace_i, :])
        den_sum_4 = den_sum_4 + traces[trace_i, :] * traces[trace_i, :]

    ############## Outside the sums ##############

    # Numerator
    num_result = ((num_traces * num_sum_1) - (num_sum_2 * num_sum_3))  # Result of the numerator

    # Left part of the Denominator
    den_sum_1 = (den_sum_1 * den_sum_1)  # Square the first sum of the denominator
    left_den = (den_sum_1 - (num_traces * den_sum_2))  # Calculate left part of the denominator

    # Right part of the Denominator
    den_sum_3 = (den_sum_3 * den_sum_3)
    right_den = (den_sum_3 - (num_traces * den_sum_4))

    new_result = (num_result / np.sqrt(left_den * right_den))

    ####################################### Old Formula ######################################
    for trace_i in range(0, num_traces):
        h_diff = (hyp[trace_i] - h_mean)  # Difference of hypothesis value
        t_diff = traces[trace_i, :] - t_mean  # Difference of traces value

        sum_num = sum_num + (h_diff * t_diff)  # Sum of the numerator
        sum_den_1 = sum_den_1 + h_diff * h_diff  # Left Sum of the denominator
        sum_den_2 = sum_den_2 + t_diff * t_diff  # Right Sum of the denominator

    ############## Outside the sums ##############

    fraction_result = sum_num / np.sqrt(sum_den_1 * sum_den_2)

    ############## Prints ##############

    # print(num_result)
    # print(sum_num)

    # print(left_den)
    # print(sum_den_2)

    # print(right_den)
    # print(sum_den_2)

    print(new_result)
    print(fraction_result)

    return new_result  # Calculate the output online cpa value


# Go through all the different hypothesis
def check_sub_key(num_point, num_traces, plain_txt, sub_key, HW, traces, cpa_output, max_cpa):
    """
    Performs all the execution for a sub-key
    """
    # Go through all the different hypothesis
    for k_guess in range(0, SIZE):
        # print("Subkey %2d, hyp = %02x: " % (sub_key, k_guess)),

        # Set to zeros according to the total number of traces -> N
        [sum_num, sum_den_1, sum_den_2] = to_zero(3, num_point)

        hyp = np.zeros(num_traces)  # Set to zeros

        # Get the hypothesis for the trace
        for trace_i in range(0, num_traces):  # TODO No idea why
            sbox_output = intermediate(plain_txt[trace_i][sub_key], k_guess)  # Get the sbox output
            hyp[trace_i] = HW[sbox_output]  # Get the amount of 1s of the integer from the output of the sbox

        h_mean = np.mean(hyp, dtype=np.float64)  # Mean of hypothesis
        t_mean = np.mean(traces, axis=0, dtype=np.float64)  # Mean of all points in trace

        # For each trace calculate the formula
        cpa_output[k_guess] = calculate_formula(traces, num_traces, hyp, h_mean, t_mean,
                                                sum_num, sum_den_1, sum_den_2,
                                                num_point)

        max_cpa[k_guess] = max(abs(cpa_output[k_guess]))

    # print(max_cpa[k_guess])
    return max_cpa


def online_CPA(input_num_traces, input_sub_key_amount):
    print("Online CPA Execution: Traces:{} \tSub key:{}".format(input_num_traces, input_sub_key_amount))

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
        max_cpa = check_sub_key(num_point, num_traces, plain_txt, sub_key, HW, traces, cpa_output, max_cpa)

        # Get the best guess
        best_guess[sub_key] = np.argmax(max_cpa)

        # Sort max_cpa
        cpa_refs = np.argsort(max_cpa)[::-1]

        # Find GE accessing to the known key
        ge[sub_key] = list(cpa_refs).index(known_key[0][sub_key])  # TODO I don't know why that 0

    print_result(best_guess, ge)
    save_result(ONLINE_CPA_FOLDER, best_guess, ge, input_sub_key_amount, num_traces)

    return 0
