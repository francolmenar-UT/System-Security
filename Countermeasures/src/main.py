from functions.crypto import create_key
from functions.packet_prepare import create_message
import numpy as np

from src.square_mult import square_mult

msg = 100

e, d, n, key = create_key()

print("n: {}".format(n))
print("e: {}".format(e))
print("d: {}".format(d))
print("msg: {}".format(msg))

enc = square_mult(msg, e, n)

print("enc: {}".format(enc))

dec = square_mult(enc, d, n)

print("dec: {}".format(dec))
