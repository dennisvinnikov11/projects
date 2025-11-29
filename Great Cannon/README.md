# lab6.py Usage
python3 lab6.py
## Program details
In case if the file "both_sidechannel.tcpdump" is present in the current directory, the program will print out all sessions that have incrementing TTLs.
Besides that, it will show the  number of potential GC hijacked flows, and number of likely GFW flows.
The way lab6.py does it, is by first looking at all sessions, then only printing out the ones that are not filled with the same TTL values across all packets using all() function. 
Then in the similar fashion it checks if each of the flows has incrementing TTLs by the value of 1. In that case the variable num_gc is incremented. 
If that is not the case then the variable num_gfw is incremented. At the end the program prints out these values.
In case user needs to read another file, the line 6 must be changed in the lab6.py. z = rdpcap("name_of_your_file")
