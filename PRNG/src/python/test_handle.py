import os
import time
from constants import *


def test_handle(test_list):
    """
    Receives the list with the tests to execute from the cli
    Calls the switch which calls to the methods of each test

    :param test_list: List with all the tests to run
    :return:
    """

    for test in test_list:
        switch(test)


def switch(x):
    """
    Switch implementation
    Calls to the methods for each test

    :param x: Element to consider
    :return: Case in x
    """
    return {
        '1': test_1(),
        '2': "",
    }[x]


def test_1():
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "100000000000000 "  # Just the first
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, output_file,
                               bit_streams,
                               file_format,
                               test_program, total_bit_length))
