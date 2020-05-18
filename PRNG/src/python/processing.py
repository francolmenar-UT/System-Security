from constants import *
import os


def call():
    """
    Runs the C program
    """
    os.system("./{} "
              "{} {} "
              "> {}{}".format(c_program,
                              test_bit_streams, test_total_bit_length * post_val,
                              # Set the length of the output streams
                              process_path, output_file_pre))


def process_line(line):
    """
    Performs the processing of data for the given line
    """
    new_line = ""  # Variable which will store the processed line
    for_index = int((len(line) - 1) / 2)  # - 1 because of the end of line
    remainder_index = (len(line) - 1) % 2  # Remainder for error checking

    if remainder_index != 0:  # Check that the bit stream has a correct length to process it
        print("Wrong bit stream length. It has to be multiple of 2")
        return -1

    for i in range(0, for_index):  # Go through all the chars of the line 2 by two
        # TODO Apply the post processing as it is explained in the slides

        aux = line[i * 2 + 2]
        new_line += line[i * 2] + line[i * 2 + 1]

        if i == for_index:  # Last char - It does not reach here
            print("i: {} with real index {}".format(i, i * 2))
            # line[i * 2 + 2] is the new line char
            print("Exiting, last char = {} with real index {}".format(line[i * 2 + 2], i * 2 + 2))

    return new_line + '\n'


def post_processing():
    """
    Handles the data processing methods
    """
    call()  # Call to the c file to generate the raw data

    output_f = open(output_path_test + output_file, "w+")  # Open the output file for the processed data

    with open(process_path + output_file_pre) as input_f:  # Read the pre processed data
        for line in input_f:  # Go line by line
            new_line = process_line(line)

            # TODO check that the length of the obtained line is the expected
            # TODO If not call again with itself as a concatenated bit stream

            if new_line == -1:  # Error checking
                return -1
            output_f.write(new_line)

    input_f.close()
    output_f.close()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    # conines = [line.rstrip('\n') for line in file]
