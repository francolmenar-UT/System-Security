# Paths to the folders
test_path = "../../sts-2.1.2/"
test_path_c = "../sts-2.1.2/" # From the c Program
program_path = "../../cmake-build-debug/"
output_path = "output/bit_streams/"
output_path_test = "../output/bit_streams/"  # From the executable of tests
test_obj = "obj/"
report_path = "sts-2.1.2/experiments/AlgorithmTesting/finalAnalysisReport.txt"  # Path to the resulting report
results_path = "output/analysis/"

# Programs path
c_program = "prng"
test_program = "./assess"

# Files Name
output_file = "output.txt"
test10_file = "test10.txt"
test12_13_file = "test12.txt"
analysis = "finalAnalysisReport"

# Variables for test
total_bit_length = 10000
bit_streams = 1000
file_format = 0  # ASCII [0] and Binary [1]
exec_string = ["0", "0", "0", "0", "0",  # Represents the tests which are going to be executed
               "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0"]

# Variables for Test 10
exec_test_10 = ["0", "0", "0", "0", "0",  # Special Execution for test 10
                "0", "0", "0", "0", "1",
                "0", "0", "0", "0", "0"]

exe_10 = "000000000100000"
bit_streams_test_10 = 5
total_bit_length_test_10 = 5242880

# Variables for Test 12
exec_test_12 = ["0", "0", "0", "0", "0",  # Special Execution for test 12
                "0", "0", "0", "0", "0",
                "0", "1", "0", "0", "0"]

exe_12 = "000000000001000"
bit_streams_test_12_13 = 5
total_bit_length_test_12_13 = 1000000

# Variables for Test 13
exec_test_13 = ["0", "0", "0", "0", "0",  # Special Execution for test 13
                "0", "0", "0", "0", "0",
                "0", "0", "1", "0", "0"]

exe_13 = "000000000000100"

# Variables for Test 12 & 13
exec_test_12_13 = ["0", "0", "0", "0", "0",  # Special Execution for test 12 & 13
                   "0", "0", "0", "0", "0",
                   "0", "1", "1", "0", "0"]

exe_12_13 = "000000000001100"


# The sixth requires 32x32 bits -> Handled by increasing the size
# The 10th is different -> Handled special case created
additional_par = [False, True, False, False, False,
                  False, False, True, True, False,
                  True, False, False, True, True]
