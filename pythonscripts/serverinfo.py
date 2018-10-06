#!/usr/bin/python

import os

os.system("hostname")
os.system("date +%Y%M%d")
os.system("dmidecode -t system | grep Manu")
