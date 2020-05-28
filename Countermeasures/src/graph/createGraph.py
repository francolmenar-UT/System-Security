import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.constants.constants import *


def create_graph():
    data = readfiles([MULT_FOLDER_PATH + MULT_FILE_PATH,
                      MULT_ALW_FOLDER_PATH + MULT_ALW_FILE_PATH,
                      MULT_LD_FOLDER_PATH + MULT_LD_FILE_PATH])

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
    for idx, arr in enumerate(data):  # Single graphs
        x = data[idx][EXE_COL]
        y = data[idx][EXP_COL]

        x_axis = np.arange(X_AXIS[0], X_AXIS[1], X_AXIS[2])
        y_axis = np.arange(Y_AXIS[0], Y_AXIS[1], Y_AXIS[2])

        plt.plot(x, y, 'o', label=LABEL[idx], markersize=np.sqrt(POINT_SIZE), color=COLOUR[idx])

        plt.xticks(x_axis)
        plt.yticks(y_axis)

        plt.title(NAME[idx])
        plt.xlabel(AXIS[0])
        plt.ylabel(AXIS[1])

        lgnd = plt.legend(loc="lower right", numpoints=1, fontsize=10)
        lgnd.legendHandles[0]._legmarker.set_markersize(6)

        # plt.grid(True)

        plt.grid(True, color=COLOUR[idx], alpha=0.3,  linestyle=GRID_LINESTYLE)

        print(IMG_FOLDER_PATH + IMG[idx] + ".png")

        plt.savefig(IMG_FOLDER_PATH + IMG[idx] + ".png", dpi=600)
        plt.close()

    
