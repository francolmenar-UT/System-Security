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


def print_flags(flags_l):
    arrow = "---->"
    for idx, flag in enumerate(flags_l):
        if idx > 8:
            arrow = "--->"
        print("Pcap file: {} {} Flag {}: {} \t Flag {}: {} \t Flag {}: {}".format(
            idx + 1, arrow, flag[0][0], flag[0][1], flag[1][0], flag[1][1], flag[2][0], flag[2][1], ))


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

flags_list = []

# Get the flags from the packets
for reader in reader_list:
    set_pk = set([])
    six_ten_ctn, eight_ten_ctn, twenty_four_ctn = 0, 0, 0

    for pkt in tqdm(reader):
        flags = pkt.payload.payload.flags

        six_ten_ctn = six_ten_ctn + 1 if flags == 16 else six_ten_ctn

        eight_ten_ctn = eight_ten_ctn + 1 if flags == 18 else eight_ten_ctn

        twenty_four_ctn = twenty_four_ctn + 1 if flags == 24 else twenty_four_ctn

        set_pk.add(flags)

    pk_list = list(set_pk)
    pk_list = [int(x) for x in pk_list]
    pk_list.sort()

    flags_list.append([[pk_list[0], six_ten_ctn],
                       [pk_list[1], eight_ten_ctn],
                       [pk_list[2], twenty_four_ctn]])


print_flags(flags_list)
