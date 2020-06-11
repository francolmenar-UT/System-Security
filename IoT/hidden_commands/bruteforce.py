from itertools import combinations_with_replacement as combinations
import os
from tqdm import tqdm
import string
import time

alphabet = list(string.ascii_letters+string.digits)

f = open('messages.txt', 'w')

for comb in tqdm(combinations(alphabet, 3)):
    st = ''.join(comb)
    os.system('mosquitto_pub -h localhost -p 8888 -t led/wemos25/action -m {}'.format(st))
    f.write('{}\n'.format(st))
    #time.sleep(1)
