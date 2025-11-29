# Host Discovery
I wrote this tool to passively discover hosts within a local network during my penetration testing project at Hotstart. It's a less intrusive way to discover potential targets, that actively communicate with the current host. This program takes a packet capture file, and parses through its Layer 3 data, to retrieve unique IP addresses. Then those IPs are written into a "doscovered_hosts.txt" file, which is formated in a way that can be easily used by nmap to further scan thos hosts for vulnerabilities. This script can also check whether the hosts are still reachable.

### Dependenices:
This script requires scapy library.
It can be installed on a debian-based system using
```
sudo apt install python3-scapy
```
or 
```
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
pip install scapy
```

### Usage:
```
python3 host_discovery.py <your_pcapfile>
```
For your convenience I have provided "smtp.pcap" file, if you would like to test this script.
