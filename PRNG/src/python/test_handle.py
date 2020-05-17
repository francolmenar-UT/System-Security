import os
from constants import *


def test_handle(test_list):
    """
    Receives the list with the tests to execute from the cli

    :param test_list: List with all the tests to run
    :return:
    """

    is_additional = ""  # Check if there is any input which needs additional parameters

    # Update the String of Executing tests
    for i, item in enumerate(test_list):
        exec_string[int(item) - 1] = '1'

        # Checks if there is any test with additional parameters
        if additional_par[int(item) - 1] is True:
            is_additional = "0"

    # Special execution for test 10
    if exec_string == exec_test_10:
        run_test_10(is_additional)
        return
    
    # Special execution for test 12 & 13
    if exec_string == exec_test_12 or exec_string == exec_test_13 or exec_string == exec_test_12_13:
        run_test_12_13(is_additional)
        return
    
    run_tests(is_additional)


def run_tests(is_additional):
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, output_file,
                               ''.join(exec_string),
                               is_additional,
                               bit_streams,
                               file_format,
                               test_program, total_bit_length))


def run_test_10(is_additional):
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, test10_file,
                               ''.join(exec_string),
                               is_additional,
                               bit_streams_test_10,
                               file_format,
                               test_program, total_bit_length_test_10))


def run_test_12_13(is_additional):
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, test12_13_file,
                               ''.join(exec_string),
                               is_additional,
                               bit_streams_test_12_13,
                               file_format,
                               test_program, total_bit_length_test_12_13))