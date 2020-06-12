from kamene.all import *

from os import listdir
from os.path import isfile, join

from src.const.const import PCAP_PATH

# Read the pcap files
pcap_files = [f for f in listdir(PCAP_PATH) if isfile(join(PCAP_PATH, f))]

# Sort them alphabetically
pcap_files.sort()

# List with all the reader files
reader_list = []

# Get all the readers for the different pcap files
for pcap in pcap_files:
    reader_list.append(PcapReader(PCAP_PATH + pcap))



