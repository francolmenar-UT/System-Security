E = [  # Exponent Ranges to be used
    3,
    1000000000  # 25.000.000.000
]
# Increasing step for the key size
E_STEP = 100000  # 100.000

N = 27717198807036709102711477657025983617502189422543517905554501821161346254130760336204092270200197509467985755394526028473796034663721327054486638927175954564808691810080519062784197427810586161599679574597325760584115699356926794000564365281475555146315301171339698824702726078232606714100029908329093194873169775904214268411350637699128923863579883976112406497794312324708356527742150589471693240852100363708141384315549913115049080003062029528488019729045406176208958331530172506084228295609516491963165404242917465291446904267476177696488980842033713996568489235543578188484252001277672931897068216357192983696503

MSG = 17551448821259686233315701109500236998071404084358796433141172148072603561736027317147277765044032727860189328930735626526591703316588219108526285701613280171301103939952824022160720139921242668064605237287789459154542097350195258756964747514367458008184355494827212650769494978750215285955523701630170875836246534961676140162162941552475479216691416777559856575157339803666628650373331312353158706504973504388538699782617201259154489832523929758588198160578557114975256568889580568147408314734000047881948830766807812245950162445036357935829752126984665445505205742326719491756624691913523882724541354894177719425497

MIN = 0  # Index in the lists for the maximum value
MAX = 1  # Index in the lists for the maximum value

EXE_REP = 50

KEY_FOLDER_PATH = "data/keys/"
KEY_FILE_PATH = "keys.csv"

MULT_FOLDER_PATH = "data/square_mult/"
MULT_FILE_PATH = "square_mult_results.csv"

MULT_ALW_FOLDER_PATH = "data/square_mult_alw/"
MULT_ALW_FILE_PATH = "square_mult_alw_results.csv"

MULT_LD_FOLDER_PATH = "data/ladder/"
MULT_LD_FILE_PATH = "ladder.csv"
IMG_FOLDER_PATH = "img/"

EXP_COL = "Exponent"
EXE_COL = "Execution time"

IMG = [
    "square_mult",
    "square_mult_alw",
    "ladder"
]

COLOUR = [
    "tab:blue",
    "tab:orange",
    "tab:green"
]

GRID_COLOUR = '#cfe0e8'
GRID_LINESTYLE = '--'

LABEL = [
    "Square-and-multiply",
    "Square-and-multiply always",
    "Montgomery Ladder"
]

NAME = [
    "Square-and-multiply Algorithm",
    "Square-and-multiply Always Algorithm",
    "Montgomery Ladder Algorithm"
]

NAME_AUX = [
    "Square-and-multiply",
    "Square-and-multiply Always",
    "Montgomery Ladder"
]

AXIS = [
    "Execution time (s)",
    "Exponent value (1e6)"
]

X_AXIS = [0.0,
          0.11,
          0.01
          ]

Y_AXIS = [0,
          6000,
          500]

POINT_SIZE = .25
