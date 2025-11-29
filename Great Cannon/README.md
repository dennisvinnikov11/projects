# Great Cannon Project
This was one of my favorite projects at Eastern Washington University. In this project I was given a tcpdump file of a traffic where I needed to identify packets comming from Chinese censorship tools Great Cannon and Great Firewall based on known signatures, and differentiate between them. Great Firewall is a passive tool that would send RST packets to hosts involved in a connection that is violating Chinese Government policies. Great Cannon builds on that, where it also injects a malicious javascript that then uses injected hosts to DDoS anti-cencorship websites.

Link to the Research Article:
https://www.usenix.org/system/files/conference/foci15/foci15-paper-marczak.pdf

# Usage
python3 lab6.py
## Program details
In case if the file "both_sidechannel.tcpdump" is present in the current directory, the program will print out all sessions that have incrementing TTLs.
Besides that, it will show the  number of potential GC hijacked flows, and number of likely GFW flows.
The way lab6.py does it, is by first looking at all sessions, then only printing out the ones that are not filled with the same TTL values across all packets using all() function. 
Then in the similar fashion it checks if each of the flows has incrementing TTLs by the value of 1. In that case the variable num_gc is incremented. 
If that is not the case then the variable num_gfw is incremented. At the end the program prints out these values.
