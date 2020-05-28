import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.constants.constants import *


def create_graph():
    data = readfiles([MULT_FOLDER_PATH + MULT_FILE_PATH,
                      MULT_ALW_FOLDER_PATH + MULT_ALW_FILE_PATH,
                      MULT_LD_FOLDER_PATH + MULT_LD_FILE_PATH])

    plt_counter = 0
    for idx, arr in enumerate(data):  # Single graphs
        createPlots(EXE_COL, EXP_COL, data[idx], LABEL[idx], COLOUR[idx],
                    X_AXIS, Y_AXIS, POINT_SIZE, NAME[idx], AXIS,
                    GRID_LINESTYLE)
        plt_counter += 1

        lgnd = plt.legend(loc="lower right", numpoints=1, fontsize=10)
        for i in range(0, plt_counter):
            lgnd.legendHandles[i]._legmarker.set_markersize(POINT_SIZE_LEGEND)

        plt.savefig(IMG_FOLDER_PATH + IMG[idx] + ".png", dpi=600)
        plt.close()
        plt_counter = 0

    plt_counter = 0
    for idx, arr in enumerate(data):  # Multiple graphs
        name = ""
        name_plt = ""
        if idx == len(data) - 1:
            break
        else:
            name += IMG_FOLDER_PATH + IMG[idx]
            name_plt += NAME_AUX[idx]
            createPlots(EXE_COL, EXP_COL, data[idx], LABEL[idx], COLOUR[idx],
                        X_AXIS, Y_AXIS, POINT_SIZE, NAME[idx], AXIS,
                        GRID_LINESTYLE, grid_colour=GRID_COLOUR)
            plt_counter += 1

        for i in range(idx + 1, len(data)):  # Each graph prints the comparison with the following ones
            createPlots(EXE_COL, EXP_COL, data[i], LABEL[i], COLOUR[i],
                        X_AXIS, Y_AXIS, POINT_SIZE, NAME[i], AXIS,
                        GRID_LINESTYLE, grid_colour=GRID_COLOUR)
            plt_counter += 1

            name += " & " + IMG[i]
            name_plt += " & \n" + NAME_AUX[i]

        lgnd = plt.legend(loc="lower right", numpoints=1, fontsize=10)
        for i in range(0, plt_counter):
            lgnd.legendHandles[i]._legmarker.set_markersize(POINT_SIZE_LEGEND)

        plt.title(name_plt)
        plt.savefig(name + ".png", dpi=600)

        plt.close()
        plt_counter = 0

    plt_counter = 0
    for idx, arr in enumerate(data):  # Two graphs - Not last
        if idx == len(data) - 2:  # The two last ones are handled in the loop before
            break

        for i in range(idx + 1, len(data)):  # Each graph prints the comparison with one of the following ones
            name = IMG_FOLDER_PATH + IMG[idx]  # Base graph
            name_plt = NAME_AUX[idx]
            createPlots(EXE_COL, EXP_COL, data[idx], LABEL[idx], COLOUR[idx],
                        X_AXIS, Y_AXIS, POINT_SIZE, NAME[idx], AXIS,
                        GRID_LINESTYLE, grid_colour=GRID_COLOUR)
            plt_counter += 1

            name += " & " + IMG[i]
            name_plt += " & \n" + NAME_AUX[i]

            createPlots(EXE_COL, EXP_COL, data[i], LABEL[i], COLOUR[i],  # Graph compared to
                        X_AXIS, Y_AXIS, POINT_SIZE, NAME[i], AXIS,
                        GRID_LINESTYLE, grid_colour=GRID_COLOUR)
            plt_counter += 1

            lgnd = plt.legend(loc="lower right", numpoints=1, fontsize=10)
            for i in range(0, plt_counter):
                lgnd.legendHandles[i]._legmarker.set_markersize(POINT_SIZE_LEGEND)

            plt.title(name_plt)
            plt.savefig(name + ".png", dpi=600)
            plt.close()
            plt_counter = 0


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


def createPlots(c1, c2, data, label, colour,
                x_axis, y_axis, point_size, name, axis,
                grid_linestyle, grid_colour=None):
    x = data[c1]
    y = data[c2]

    x_axis = np.arange(x_axis[0], x_axis[1], x_axis[2])
    y_axis = np.arange(y_axis[0], y_axis[1], y_axis[2])

    plt.plot(x, y, 'o', label=label, markersize=np.sqrt(point_size), color=colour)

    plt.xticks(x_axis)
    plt.yticks(y_axis)

    plt.title(name)
    plt.xlabel(axis[0])
    plt.ylabel(axis[1])

    if grid_colour is None:
        plt.grid(True, color=colour, alpha=0.3, linestyle=grid_linestyle)
    else:
        plt.grid(True, color=grid_colour, linestyle=grid_linestyle)
