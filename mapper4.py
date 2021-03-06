#!/usr/bin/python

'''
Find the total number of hits to each file on a server, using the server log file. 
The logfile is in Common Log Format:
IP id usrname [date time] "GET /path/to/page HTTP/1.1" 200 10469
e.g.
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

Use the page as key, and choose some value to pass to the reducer. I need to 
write them out to standard output, separated by a tab
key,value = page, status
'''

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, usrid, usrname, time, zone, reqtype, page, protocol, status, size = data
		print "{0}\t{1}".format(page, status)

