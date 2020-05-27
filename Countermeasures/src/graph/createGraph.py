import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.constants.constants import MULT_FOLDER_PATH, MULT_FILE_PATH, EXP_COL, EXE_COL, IMG_FOLDER_PATH, IMG


def create_graph():
    data = readfiles([MULT_FOLDER_PATH + MULT_FILE_PATH])

    createPlots(data)


def readfiles(files):
    data = []
    c1 = EXP_COL
    c2 = EXE_COL
    for file in files:
        data_tmp = pd.read_csv(file, sep=",", header=None, names=[c1, c2])

        # round numbers and convert
        data_tmp[c1] = round(data_tmp[c1].astype(float) / 1e6)

        # insert zero in both columns at index 1
        line = pd.DataFrame({c1: 0, c2: 0}, index=[0])
        data_tmp = pd.concat([data_tmp.iloc[:0], line, data_tmp.iloc[0:]]).reset_index(drop=True)
        data.append(data_tmp)
    return data


def createPlots(data):
    for idx, arr in enumerate(data):
        x = data[idx][EXE_COL]
        y = data[idx][EXP_COL]

        plt.plot(x, y, 'o', label='square mult', markersize=np.sqrt(15.))

        # b, m = polyfit(x, y, 1)
        # plt.plot(x, b + m * x, '-')

        plt.title('Title')
        plt.xlabel("Execution time (s)")
        plt.ylabel("Exponent value (1e6)")

        lgnd = plt.legend(loc="lower right", numpoints=1, fontsize=10)
        lgnd.legendHandles[0]._legmarker.set_markersize(6)

        # plt.grid(True)

        plt.grid(True, color='#cfe0e8', linestyle='--')

        plt.savefig(IMG_FOLDER_PATH + IMG[idx] + ".png", dpi=600)