#!/usr/bin/env python
from scapy.all import *
import sys
import os


def main():
    pcap_file = sys.argv[1]
    z = rdpcap(pcap_file)
    ses = z.sessions()
    print("Reading pcap:")


    addresses = []
    for key, value in ses.items():
        for i, s in enumerate(value):
            if IP in s:
                src_address = s[IP].src
                dst_address = s[IP].dst
                if src_address not in addresses:
                    addresses.append(src_address)
                if dst_address not in addresses:
                    addresses.append(dst_address)
    write_list_to_file(addresses)
    print("Do you want  to see if the hosts are reqchable? Y/n \n")
    user_response = input()
    if user_response.upper() == 'Y':
        for i in range(len(addresses)):
            host_is_up(addresses[i])
    elif user_response.upper() == 'N':
        print("Ok :(")

def host_is_up(ip_addr):
    os.system(f"ping -c 1 {ip_addr}")

def write_list_to_file(list):
    f = open("discovered_hosts.txt", "w")
    for i in range(len(list)):
        f.write(list[i] + '\n')
    print("The results are saved to discovered_hosts.txt")


if __name__ == "__main__":
    main()

