import os
from constants import *


def test_handle(test_list):
    """
    Receives the list with the tests to execute from the cli

    :param test_list: List with all the tests to run
    :return:
    """

    is_additional = ""  # Check if there is any input which needs additional parameters
    output_name = analysis  # Used for copying the files and setting the right name
    is_test_10 = False
    is_test_12 = False
    is_test_13 = False

    if 10 in test_list:
        is_test_10 = True
        test_list.remove(10)

    if 12 in test_list:
        is_test_12 = True
        test_list.remove(12)

    if 13 in test_list:
        is_test_13 = True
        test_list.remove(13)

    # Update the String of Executing tests
    for i, item in enumerate(test_list):
        exec_string[int(item) - 1] = '1'

        # Checks if there is any test with additional parameters
        if additional_par[int(item) - 1] is True:
            is_additional = "0"

    if len(test_list) > 0:  # Run the normal tests
        run_tests(is_additional)

    # The rest of tests does not need the additional arguments
    is_additional = ""

    # Special execution for test 10
    if is_test_10:
        run_test_10(is_additional, exe_10, output_name + "_10.txt")

    # Special execution for test 12 & 13
    if is_test_12 and is_test_13:
        run_test_12_13(is_additional, exe_12_13, output_name + "_12-13.txt")
        return

    elif is_test_12:
        run_test_12_13(is_additional, exe_12, output_name + "_12.txt")

    elif is_test_13:
        run_test_12_13(is_additional, exe_13, output_name + "_13.txt")

    return


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

    os.system("cp ../{} ../{}".format(report_path, results_path))


def run_test_10(is_additional, exe_10, output_name):
    print("echo '0' "  # Select option input file
          "{}{} "  # Path to the output file
          "0 "  # Choose the tests
          "{} "  # Execution String of tests
          "{} "  # Additional parameters
          "{} "  # Amount of bit-streams
          "{} "  # ASCII [0] or Binary [1]
          "| {} {}".format(output_path_test, test10_file,
                           exe_10,
                           is_additional,
                           bit_streams_test_10,
                           file_format,
                           test_program, total_bit_length_test_10))

    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, test10_file,
                               exe_10,
                               is_additional,
                               bit_streams_test_10,
                               file_format,
                               test_program, total_bit_length_test_10))

    os.system("cp ../{} ../{}{}".format(report_path, results_path, output_name))


def run_test_12_13(is_additional, exe_12_13, output_name):
    os.system("echo '0' "  # Select option input file
              "{}{} "  # Path to the output file
              "0 "  # Choose the tests
              "{} "  # Execution String of tests
              "{} "  # Additional parameters
              "{} "  # Amount of bit-streams
              "{} "  # ASCII [0] or Binary [1]
              "| {} {}".format(output_path_test, test12_13_file,
                               exe_12_13,
                               is_additional,
                               bit_streams_test_12_13,
                               file_format,
                               test_program, total_bit_length_test_12_13))

    os.system("cp ../{} ../{}{}".format(report_path, results_path, output_name))
