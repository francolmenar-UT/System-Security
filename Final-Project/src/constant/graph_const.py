########################### Values for reading the CSV files ###########################
# Rounding value for the execution time. If it is set to None no round is performed
ROUND_VAL = 2

# Names for the columns of the np array
COL_NM = ["Attack Size",
          "Partial GE"]

########################### Constants for Graph Creation  ###########################
# Range of values for the axis
AXIS = [
    [0, 5000, 500],
    [0, 275, 25]
]

# Names for the axis
AXIS_NM = [
    "Attack Size",
          "Partial GE"
]

# Colours for the different graphs
COLOUR = [
    "tab:blue",
    "coral",
    "tab:green",
    "gold"
]

COLOUR_FILL_MEDIAN = "cornflowerblue"

# Default colour for the grid for comparison graphs
GRID_COLOUR = '#cfe0e8'

IMG_FOLDER_PATH = "img/"

# Name for the images files
IMG = [
    "scenario_1_noise",
    "scenario_1",
    "scenario_2_noise",
    "scenario_2"
]

IMG_SIZE = 600

# Type of the output image file
IMG_TYPE = ".png"

# Names for the labels from the legend
LABEL = [
    "Scenario 1 with noise",
    "Scenario 1 without noise",
    "Scenario 2 with noise",
    "Scenario 2 without noise"
]

# Names for the different graphs
GRAPH_NM = [
    "Scenario 1 with noise",
    "Scenario 1 without noise",
    "Scenario 2 with noise",
    "Scenario 2 without noise"
]

# Names for the comparison graphs
GRAPH_COMP_NM = [
    "Scenario 1 with noise",
    "Scenario 1 without noise",
    "Scenario 2 with noise",
    "Scenario 2 without noise"
]

# Size of the points for the graph
PTN_SIZE = [3,  # For graph with points
              3]  # For discontinuous line graphs

# Size for the points for the legend
PTN_SIZE_LGN = 3

############# Modes for the legend of the graphs  #############
LGN_LR = "lower right"

############# Modes for the graphs  #############
PTN = "POINT"
PTN_F = "points/"

LN_DISC = "LN_DISC"
LN_DISC_F = "line_disc/"

LN_MEDIAN = "LN_MEDIAN"
LN_MEDIAN_F = "line_median/"

VLN = "VLN"
VLN_F = "violin/"

ALL_MODES = [PTN, LN_DISC, VLN]
MODE_F = [PTN_F, LN_DISC_F, LN_MEDIAN_F, VLN_F]

############# Modes for the Grid Linestyle  #############
GRID_DISC = '--'

