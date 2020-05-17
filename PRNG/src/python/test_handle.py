import os
from constants import *


def run_test(test_path, is_additional, exe, bit_stream, total_bit_length, output_name):
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, test_path,
                               exe,
                               is_additional,
                               bit_stream,
                               file_format,
                               test_program, total_bit_length))

    os.system("cp ../{} ../{}{}".format(report_path, results_path, output_name))


def check_case(test_list, value):
    """
    Checks if a value is in the list. If it is, it is removed and True is returned
    :param test_list: List of executing tests
    :param value: Test to search
    :return: True if the value is found, False otherwise
    """
    if value in test_list:
        test_list.remove(value)
        return True
    return False


def test_handle(test_list):
    """
    Receives the list with the tests to execute from the cli
    :param test_list: List with all the tests to run
    """
    is_additional = ""  # Check if there is any input which needs additional parameters
    output_name = analysis  # Used for setting the name of the resulting analysis files

    # Check for special case test executions
    is_test_10 = check_case(test_list, 10)
    is_test_12 = check_case(test_list, 12)
    is_test_13 = check_case(test_list, 13)

    # Transforms the list to a 0s and 1s list
    for i, item in enumerate(test_list):
        exec_string[int(item) - 1] = '1'

        # Checks if there is any test with additional parameters
        if additional_par[int(item) - 1] is True:
            is_additional = "0"

    if len(test_list) > 0:  # Run the normal tests
        # run_tests(is_additional)

        run_test(output_file, is_additional, ''.join(exec_string),
                 bit_streams, total_bit_length,
                 "")

    is_additional = ""  # The rest of tests does not need the additional arguments

    # Special execution for test 10
    if is_test_10:
        run_test(test10_file, is_additional, exe_10,
                 bit_streams_test_10, total_bit_length_test_10,
                 output_name + "_10.txt")

    # Special execution for test 12 & 13
    if is_test_12 and is_test_13:
        run_test(test12_13_file, is_additional, exe_12_13,
                 bit_streams_test_12_13, total_bit_length_test_12_13,
                 output_name + "_12-13.txt")
        return 0

    elif is_test_12:
        run_test(test12_13_file, is_additional, exe_12,
                 bit_streams_test_12_13, total_bit_length_test_12_13,
                 output_name + "_12.txt")

    elif is_test_13:
        run_test(test12_13_file, is_additional, exe_13,
                 bit_streams_test_12_13, total_bit_length_test_12_13,
                 output_name + "_13.txt")
    return 0
