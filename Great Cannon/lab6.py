#! /usr/bin/env python
from scapy.all import *
def main():
    num_gc = 0
    num_gfw = 0
    z = rdpcap("both_sidechannel.tcpdump")
    ses = z.sessions()
    for key,value in ses.items():
        ttls = []
        win_sizes = []
        seq = 0
        for s in value:
            if TCP in s:
                ttls.append(s[IP].ttl)
                win_sizes.append(s[IP].window)
                seq = s[IP].seq

        # Check if the ttls are all identical in the list
        ttls_equal = all(x == ttls[0] for x in ttls)
        if ttls_equal is False:
            print("TTL values: ")
            print(ttls)
            print("Window size values")
            print(win_sizes)
            print("Sequence number: " + str(seq))
            print("===========================================================")
            ttls_incr_by_one = all(ttls[i+1] - ttls[i] == 1 for i in range(len(ttls) -1))
            if ttls_incr_by_one is True:
                num_gc += 1
            else:
                num_gfw += 1
    print("Summary")
    print("________________________________________________________")
    print("Potential GC packets found: "+ str(num_gc))
    print("Potential GFW packets found: "+ str(num_gfw))
if __name__ == "__main__":
    main()
