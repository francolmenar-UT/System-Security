from constants import *
import os


def call():
    """
    Runs the C program
    """
    os.system("./{} "
              "{} {} "
              "> {}{}".format(c_program,
                              bit_streams, total_bit_length * post_val,
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

        if line[i * 2] != line[i * 2 + 1]:  # If they are not the same the first bit is taken
            new_line += line[i * 2]  # Copy just the first one

    return new_line


def post_processing():
    """
    Handles the data processing methods
    """
    call()  # Call to the c file to generate the raw data

    output_f = open(output_path_test + output_file, "w+")  # Open the output file for the processed data

    with open(process_path + output_file_pre) as input_f:  # Read the pre processed data
        for line in input_f:  # Go line by line
            new_line = ""  # Reset the new line to be added

            # Process the line until the length is at least the defined bit stream length
            while len(new_line) < total_bit_length:
                new_line += process_line(line)  # Append the newly processed line

            new_line = new_line[:total_bit_length] + '\n'

            if new_line == -1:  # Error checking
                return -1
            output_f.write(new_line)  # Write the processed line to the output text file

    input_f.close()
    output_f.close()
    return 0
