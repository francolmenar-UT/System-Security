# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:08:22 2020

@author: stjepan
"""

import numpy as np

from src.constants.constants import *


def intermediate(plain_txt, key_guess):
    return SBOX[plain_txt ^ key_guess]  # Just XOR???


def CPA():
    HW = [bin(n).count("1") for n in range(0, SIZE)]

    traces = np.load(r'' + CHIP_FOLDER + TRACES)
    plain_txt = np.load(r'' + CHIP_FOLDER + PLAIN)
    known_key = np.load(r'' + CHIP_FOLDER + KEY)

    num_traces = np.shape(traces)[0] - 1
    num_point = np.shape(traces)[1]

    # Use less than the maximum traces by setting num_traces to something
    num_traces = NUM_TRACES

    # Set 16 to something lower (like 1) to only go through a single sub-key
    best_guess = [0] * BEST_GUESS_AUX
    ge = np.zeros(BEST_GUESS_AUX)

    for b_num in range(0, 1):  # Set just for the first sub-key
        cpa_output = [0] * SIZE
        max_cpa = [0] * SIZE
        for k_guess in range(0, SIZE):
            print("Subkey %2d, hyp = %02x: " % (b_num, k_guess)),

            # Set to zeros according to num_point
            sum_num = np.zeros(num_point)
            sum_den_1 = np.zeros(num_point)
            sum_den_2 = np.zeros(num_point)
            
            # Set to zeros
            hyp = np.zeros(num_traces)
            
            for t_num in range(0, num_traces):
                hyp[t_num] = HW[intermediate(plain_txt[t_num][b_num], k_guess)]

            # Mean of hypothesis
            h_mean = np.mean(hyp, dtype=np.float64)

            # Mean of all points in trace
            t_mean = np.mean(traces, axis=0, dtype=np.float64)

            # For each trace, do the following
            for t_num in range(0, num_traces):
                h_diff = (hyp[t_num] - h_mean)
                t_diff = traces[t_num, :] - t_mean

                sum_num = sum_num + (h_diff * t_diff)
                sum_den_1 = sum_den_1 + h_diff * h_diff
                sum_den_2 = sum_den_2 + t_diff * t_diff

            cpa_output[k_guess] = sum_num / np.sqrt(sum_den_1 * sum_den_2)
            max_cpa[k_guess] = max(abs(cpa_output[k_guess]))

            print(max_cpa[k_guess])

        best_guess[b_num] = np.argmax(max_cpa)

        cpa_refs = np.argsort(max_cpa)[::-1]

        # Find GE
        ge[b_num] = list(cpa_refs).index(known_key[0][b_num])

    for b in range(0, BEST_GUESS_AUX):
        print("Best Key Guess: ", best_guess[b], " GE: ", ge[b])

    return 0
