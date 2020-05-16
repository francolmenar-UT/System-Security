# Paths to the folders
test_path = "../../sts-2.1.2/"
program_path = "../../cmake-build-debug/"
output_path = "output/"
output_path_test = "../output/"  # From the executable of tests
test_obj = "obj/"

# Programs path
c_program = "prng"
test_program = "./assess"

# Files path
output_file = "output.txt"
test10_file = "test10.txt"

# Variables for test
total_bit_length = 1300
bit_streams = 100
file_format = 0  # ASCII [0] and Binary [1]
exec_string = ["0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0"]  # Represents the tests which are going to be executed

exec_test_10 = ["0", "0", "0", "0", "0",
                "0", "0", "0", "0", "1",
                "0", "0", "0", "0", "0"]  # Special Execution for only test 10

bit_streams_test_10 = 5
total_bit_length_test_10 = 5242880

additional_par = [False, True, False, False, False,
                  False, False, True, True, False,  # The sixth requires 32x32 bits, The 10th is different
                  True, False, False, True, True]  # The 12-13th says insufficient amount of cycles
