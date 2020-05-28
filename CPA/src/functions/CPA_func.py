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
