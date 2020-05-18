# Paths to the folders
test_path = "../../sts-2.1.2/"
test_path_c = "../sts-2.1.2/"  # From the c Program

program_path = "../../cmake-build-debug/"  # C file folder

output_path = "../output/bit_streams/"
output_path_test = "../output/bit_streams/"  # From the executable of tests

test_obj = "obj/"  # Belonging to the Test executable section
results_path = "output/analysis/"  # Path of the resulting analysis file
process_path = "../output/process_str/"  # Path to the data to be post processed

# Programs path
c_program = "prng"
test_program = "./assess"

# Files Name
output_file = "output.txt"  # Bit streams ready for running the tests
test10_file = "test10.txt"
test12_13_file = "test12.txt"

output_file_pre = "pre_output.txt"  # Bit streams to be processed
test10_file_pre = "pre_test10.txt"
test12_13_file_pre = "pre_test12.txt"

analysis = "finalAnalysisReport"
report_path = "sts-2.1.2/experiments/AlgorithmTesting/finalAnalysisReport.txt"  # Path to the resulting report

# Variables for post processing
post_val = 4  # To multiply the original length so to have enough raw data

# Variables for test
total_bit_length = 10000  # 10k
bit_streams = 1000  # 1k

file_format = 0  # ASCII [0] and Binary [1]
exec_string = ["0", "0", "0", "0", "0",  # Represents the tests which are going to be executed
               "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0"]

additional_par = [False, True, False, False, False,
                  False, False, True, True, False,
                  True, False, False, True, True]

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
