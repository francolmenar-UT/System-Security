import sys

import h5py
import numpy as np
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


def compute_tracesHW(tracesTrain, outputSboxHW):
    TracesHW = [[] for _ in range(9)]

    for i in range(len(tracesTrain)):
        HW = outputSboxHW[i]
        TracesHW[HW].append(tracesTrain[i])
    result = [np.array(TracesHW[HW]) for HW in range(9)]

    return result


def compute_key(tracesTest, features, hamming, sbox, ptTest, meanMatrix, covMatrix, knownkey, ge, best_guess, k):
    P_k = np.zeros(256)
    # For every test trace
    for j in range(len(tracesTest)):
        # Select the POI
        a = [tracesTest[j][features[i]] for i in range(len(features))]

        # For every possible key value
        for kguess in range(0, 256):
            # Get the hardware
            HW = hamming[sbox[ptTest[j][k] ^ kguess]]
            # Compute pdf
            rv = multivariate_normal(meanMatrix[HW], covMatrix)
            p_kj = rv.pdf(a)

            P_k[kguess] += np.log(p_kj)

        # Compute current GE and best_guess
        tarefs = np.argsort(P_k)[::-1]
        ge[k] = list(tarefs).index(knownkey[0][k])
        best_guess[k] = np.argsort(P_k)[-1]

    return


def pool_atack():
    """

    :return:
    """
    # Check if all the needed folders are created
    for folder in FOLDERS:
        create_folder(folder)

    # Convert the h5 file to npy to ease its use
    h5_to_npy(H5_TRACES_P) if CALC_NPY else None

    # Load the NPY data
    traces, pt, knownkey = load_data()

    # Initialize the Hamming Weight Array
    hamming = [bin(n).count("1") for n in range(256)]

    # TODO Continue Here, take the following values from inputs and this is what it is set in the pdf.
    tracesTrain = traces[0:9000]
    ptTrain = pt[0:9000]

    tracesTest = traces[9990:10000]
    ptTest = pt[9990:10000]

    outputSbox = [SBOX[ptTrain[i][0] ^ knownkey[i][0]] for i in range(len(ptTrain))]
    outputSboxHW = [hamming[s] for s in outputSbox]

    TracesHW = compute_tracesHW(tracesTrain, outputSboxHW)

    Means = np.zeros((9, len(tracesTrain[0])))
    for i in range(9):
        Means[i] = np.average(TracesHW[i], 0)

    SumDiff = np.zeros(len(tracesTrain[0]))
    for i in range(9):
        for j in range(i):
            SumDiff += np.abs(Means[i] - Means[j])

    plt.plot(SumDiff)
    plt.grid()
    # plt.show()

    features = []
    numFeatures = 5
    featureSpacing = 5
    for i in range(numFeatures):
        nextFeature = SumDiff.argmax()
        features.append(nextFeature)

        featureMin = max(0, nextFeature - featureSpacing)
        featureMax = min(nextFeature + featureSpacing, len(SumDiff))
        for j in range(featureMin, featureMax):
            SumDiff[j] = 0

    meanMatrix = np.zeros((9, numFeatures))
    covMatrix = np.zeros((numFeatures, numFeatures))
    for HW in range(9):
        for i in range(numFeatures):
            meanMatrix[HW][i] = Means[HW][features[i]]
            for j in range(numFeatures):
                x = TracesHW[HW][:, features[i]]
                y = TracesHW[HW][:, features[j]]

                c = cov(x, y)
                covMatrix[i, j] += c

    for i in range(numFeatures):
        for j in range(numFeatures):
            covMatrix[i, j] /= 9

    # print(covMatrix)
    ge = np.zeros(16)
    best_guess = np.zeros(16)

    # For each key bytes
    for k in range(16):
        compute_key(tracesTest, features, hamming, SBOX, ptTest, meanMatrix, covMatrix, knownkey, ge, best_guess, k)

    print_result(best_guess, knownkey,  ge, SUB_KEY_AMOUNT) if DEBUG else None

    # Print results
    """
    print("Traces:", j + 1)
    print("GE:", ge)
    print("Final KEY:", best_guess)
    print("Real  KEY:", knownkey[0])
    """

    return 0
