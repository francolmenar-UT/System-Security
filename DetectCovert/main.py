from kamene.all import *
from tqdm import tqdm

from os import listdir
from os.path import isfile, join

from src.const.const import *


def create_folder(folder):
    """
    Checks if a folder exists, if it does not it creates it
    :param folder: Folder to be created
    :return:
    """
    # Check if the folder does not exists
    if not os.path.isdir(folder):
        os.makedirs(folder)  # Create folder


def create_only_tcp(files):
    for f_tcp in files:
        out_f = f_tcp.split('/')
        os.system('tshark -r ' + f_tcp + ' -Y \"tcp and !http\" -w ' + ONLY_TCP_ALL_P + out_f[len(out_f) - 1])
        os.system('tshark -r ' + f_tcp + ' -Y \"tcp and !http and ip.src ==' + SRC_ADR + '\" -w ' +
                  ONLY_TCP_SRC_P + out_f[len(out_f) - 1])


def create_tcp_http(files):
    for f_tcp in files:
        out_f = f_tcp.split('/')
        os.system('tshark -r ' + f_tcp + ' -Y \"tcp and http\" -w ' + TCP_ALL_P + out_f[len(out_f) - 1])
        os.system('tshark -r ' + f_tcp + ' -Y \"tcp and http and ip.src ==' + SRC_ADR + '\" -w ' +
                  TCP_SRC_P + out_f[len(out_f) - 1])


def create_only_http(files):
    for f_tcp in files:
        out_f = f_tcp.split('/')
        os.system('tshark -r ' + f_tcp + ' -Y \"http\" -w ' + HTTP_ALL_P + out_f[len(out_f) - 1])
        os.system('tshark -r ' + f_tcp + ' -Y \"tcp and http and ip.src ==' + SRC_ADR + '\" -w ' +
                  HTTP_SRC_P + out_f[len(out_f) - 1])


def parse_pcap(files):
    # Parse the files to get only tcp
    create_only_tcp(files) if CONVERT_ONLY_TCP else None

    # Parse the files to get only tcp and http
    create_tcp_http(files) if CONVERT_TCP else None

    # Parse the files to get only http
    create_only_http(files) if CONVERT_HTTP else None


# Create the folders
for f in FOLDERS_P:
    create_folder(f)

# Read the pcap files names
pcap_files = [OR_PCAP_PA + f for f in listdir(OR_PCAP_PA) if isfile(join(OR_PCAP_PA, f))]

# Sort them alphabetically
pcap_files.sort()


parse_pcap(pcap_files)


# List with all the reader files
reader_list = []

# Read only the pcap files of TCP from the attacker phone
for pcap in pcap_files:
    last_name = pcap.split('/')
    reader_list.append(PcapReader(ONLY_TCP_SRC_P + last_name[len(last_name) - 1]))


# Print packet count just for testing
for reader in reader_list:
    packet_count = 0
    for pkt in tqdm(reader):
        packet_count = packet_count + 1

    # print(packet_count)
