import sys

import h5py
from scipy.stats import multivariate_normal
from src.functions.func import *

import matplotlib.pyplot as plt

from src.constant.constant import *


def cov(x, y):
    """
    Calculates the covariance from two numbers
    :param x:
    :param y:
    :return:
    """
    return np.cov(x, y)[0][1]


def h5_to_npy(path_f):
    """
    Save the H5 file into the different NPY files to be used
    :param path_f: Path to the H5 file
    """
    try:
        in_file = h5py.File(path_f, "r")
    except:
        print("Error: can't open HDF5 file '%s' for reading (it might be malformed) ..." % path_f)
        sys.exit(-1)

    # Get the Data from the H5 file
    raw_traces = in_file['traces'][()]
    raw_data = in_file['metadata']

    raw_plaintexts = raw_data['plaintext'][()]
    raw_keys = raw_data['key'][()]

    # Save H5 data as a Numpy Array into the defined folders
    np.save(DATA_NPY + TRACES + NPY, raw_traces)
    np.save(DATA_NPY + PLAIN + NPY, raw_plaintexts)
    np.save(DATA_NPY + KEY + NPY, raw_keys)
    return 0


def load_data():
    """
    Load the data from the NPY files
    :return: Three np arrays representing the traces, the plain text and the key
    """
    # Load the data from the NPY files
    traces = np.load(DATA_NPY + TRACES + NPY)
    pt = np.load(DATA_NPY + PLAIN + NPY)
    knownkey = np.load(DATA_NPY + KEY + NPY)

    return traces, pt, knownkey


def compute_tracesHW(traces_train, output_sbox_hw):
    """
    Calculates the HW for all the traces
    :param traces_train: Traces used to train
    :param output_sbox_hw: Output of the Sbox
    :return: The HW value for all the traces as a list of np arrays
    """
    # TODO check if the 9 means is because of the test index in the main method
    # Initialize the HW parameter
    TracesHW = [[] for _ in range(9)]

    # Go through all the traces
    for i in range(len(traces_train)):
        # Get the output of the Sbox
        HW = output_sbox_hw[i]
        # In the position of the output value from the Sbox append the actual trace
        TracesHW[HW].append(traces_train[i])

    # TODO check if the 9 means is because of the test index in the main method
    # Convert the list of lists containing the HW values to a list of np arrays
    result = [np.array(TracesHW[HW]) for HW in range(9)]

    return result


def compute_key(traces_test, features, hamming, sbox, pt_test, mean_matrix, cov_matrix, known_key, ge, best_guess,
                byte):
    """
    Compute the best key guess

    :param traces_test: Traces to test - TODO Does it means attack
    :param features: Features to be used
    :param hamming: Hamming Weight Array set to 1s
    :param sbox: Sbox defined as a constant
    :param pt_test: Plain text to be tested  - TODO Does it means attack
    :param mean_matrix: Matrix with the mean values
    :param cov_matrix: Matrix with the covariance values
    :param known_key: The actual key used
    :param ge: Guessing Entropy set to 0s
    :param best_guess: Best guess which is going to be calculated
    :param byte: The byte of the key to attack
    :return:
    """
    # Initialize P_k - It will be used to store the key guessed before returning them
    P_k = np.zeros(HW_SIZE)

    # For every test trace
    for j in range(len(traces_test)):

        # Select the POI
        a = [traces_test[j][features[i]] for i in range(len(features))]

        # For every possible key value
        for k_guess in range(0, HW_SIZE):
            # Get the HW
            HW = hamming[sbox[pt_test[j][byte] ^ k_guess]]
            # Compute pdf
            rv = multivariate_normal(mean_matrix[HW], cov_matrix)
            p_kj = rv.pdf(a)

            P_k[k_guess] += np.log(p_kj)

        # Compute current GE and best_guess
        tarefs = np.argsort(P_k)[::-1]
        ge[byte] = list(tarefs).index(known_key[0][byte])
        best_guess[byte] = np.argsort(P_k)[-1]

    return


def calc_mean(traces_train, traces_hw):
    """
    Calculate the mean value from the HW for each XXXXXX
    :param traces_train: Traces to profile
    :param traces_hw: HW values from the traces
    :return: The means from the HW
    """
    # TODO check if the 9 means is because of the test index in the main method
    # TODO check why there is a 0 there???
    # Set the mean values to 0
    means = np.zeros((9, len(traces_train[0])))

    # For each XXXX calculate the average value for the HW value TODO change XXX
    for i in range(9):
        means[i] = np.average(traces_hw[i], 0)

    return means


def calc_sum_diff(traces_train, means):
    """
    Calculates the Sum of the Difference
    :param traces_train: Traces to profile
    :param means: The means from the HW
    :return: The Sum of the Difference
    """
    # Initialize SumDiff to zeros
    SumDiff = np.zeros(len(traces_train[0]))
    # Calculate the sum of the differences TODO Check for what is this??
    for i in range(9):
        for j in range(i):
            # Get the absolute value of the difference
            SumDiff += np.abs(means[i] - means[j])

    return SumDiff


def calc_features(sum_diff):
    """
    Calculates the features and updates SumDiff
    :param sum_diff: The Sum of the Difference
    :return: The features calculated and the SumDiff
    """
    # Initialize the features to be taken
    features = []

    # Go through all the features to be considered
    for i in range(NUM_FEATURES):
        # Take the maximum value from the SumDiff
        nextFeature = sum_diff.argmax()
        # Add the next Feature
        features.append(nextFeature)

        # Get the max value from 0 to the value belonging to the next feature minus spacing
        featureMin = max(0, nextFeature - FEATURE_SPACING)
        # Get the minimum value from the value belonging to the next feature minus spacing up to the length of SumDiff
        # Which is the amount of Traces to Train
        featureMax = min(nextFeature + FEATURE_SPACING, len(sum_diff))

        # Go through every value from featureMin to featureMax
        for j in range(featureMin, featureMax):
            # Set the Sum of the difference to 0
            sum_diff[j] = 0

    return features, sum_diff


def calc_mean_cov(cov_matrix):
    """
    Updates the value of the covariance matrix by calculating its mean
    :param cov_matrix: Covariance matrix
    :return: Updated Covariance Matrix
    """
    # Calculate the mean of the covariance values
    for i in range(NUM_FEATURES):
        for j in range(NUM_FEATURES):
            cov_matrix[i, j] /= 9

    return cov_matrix


def calc_mean_cov_mat(means, features, traces_hw):
    """
    Calculate the matrices for the mean and for the covariance
    :param means: The means from the HW
    :param features: Features to be used
    :param traces_hw: HW values from the traces
    :return: The matrices for the mean and for the covariance
    """
    # Initialize the matrix of means to zero
    meanMatrix = np.zeros((9, NUM_FEATURES))

    # Initialize the matrix of covariance to zero - Square matrix of length of the number of features
    covMatrix = np.zeros((NUM_FEATURES, NUM_FEATURES))

    # Go through the HW value in XXXX #TODO Check change the value XXXX
    for HW in range(9):
        # For each HW in XXXX  go through every feature TODO
        for i in range(NUM_FEATURES):
            # Assign the value to the mean matrix
            meanMatrix[HW][i] = means[HW][features[i]]

            for j in range(NUM_FEATURES):
                # TODO Check what is happening here
                x = traces_hw[HW][:, features[i]]
                y = traces_hw[HW][:, features[j]]

                # Calculate the covariance value
                c = cov(x, y)
                # Sum the covariance value to the place in the covariance matrix
                covMatrix[i, j] += c

    return meanMatrix, covMatrix


def calc_ge_guess(traces_test, features, hamming, pt_test, mean_matrix, cov_matrix, known_key):
    """
    Calculates the GE and the Best Guess for each byte of the key analyzed
    :param traces_test:
    :param features:
    :param hamming:
    :param pt_test:
    :param mean_matrix:
    :param cov_matrix:
    :param known_key:
    :return:
    """
    # TODO change KEY_BYTES to the ones to be calculated
    # Initialize the guessing entropy
    ge = np.zeros(KEY_BYTES)
    # Initialize the best guess
    best_guess = np.zeros(KEY_BYTES)

    # For each key bytes calculate the guessed key
    for byte in range(KEY_BYTES):
        # Compute the key for the attacked key bytes
        compute_key(traces_test, features, hamming, SBOX, pt_test,
                    mean_matrix, cov_matrix, known_key, ge, best_guess, byte)

    return ge, best_guess


def pool_atack(profile_size, attack_size):
    """
    Performs the Pooled Template Attack
    :param profile_size: TODO
    :param attack_size: TODO
    """
    # Check if all the needed folders are created
    for folder in FOLDERS:
        create_folder(folder)

    # Convert the h5 file to npy to ease its use
    h5_to_npy(H5_TRACES_P) if CALC_NPY else None

    # Load the NPY data
    traces, pt, knownkey = load_data()

    # Initialize the Hamming Weight Array
    hamming = [bin(n).count("1") for n in range(HW_SIZE)]

    # Get the actual traces to be used from the total amount of traces
    # TODO Do I have to set here the values from the input???
    tracesTrain = traces[0:9000]
    ptTrain = pt[0:9000]
    tracesTest = traces[9990:10000]
    ptTest = pt[9990:10000]

    # Calculate the output of the S box
    outputSbox = [SBOX[ptTrain[i][0] ^ knownkey[i][0]] for i in range(len(ptTrain))]
    # Set the Output of the Sbox to HW
    outputSboxHW = [hamming[s] for s in outputSbox]

    # Compute the HW value for the traces
    TracesHW = compute_tracesHW(tracesTrain, outputSboxHW)

    # Compute the Mean values from the HW
    Means = calc_mean(tracesTrain, TracesHW)
    # Compute the Sum of the Difference
    SumDiff = calc_sum_diff(tracesTrain, Means)

    # Plot stuff TODO Probably remove this
    plt.plot(SumDiff)
    plt.grid()
    # plt.show()

    # Calculate the features and update SumDiff
    features, SumDiff = calc_features(SumDiff)

    # Calculate the matrices from the mean and the covariances
    meanMatrix, covMatrix = calc_mean_cov_mat(Means, features, TracesHW)

    # Calculate the mean of the covariance values
    covMatrix = calc_mean_cov(covMatrix)

    # Calculate the GE and the Best Guess for each key byte analyzed
    ge, best_guess = calc_ge_guess(tracesTest, features, hamming, ptTest, meanMatrix, covMatrix, knownkey)

    print_result(best_guess, knownkey, ge, SUB_KEY_AMOUNT) if DEBUG else None
    return 0
