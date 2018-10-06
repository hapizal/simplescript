#!/usr/bin/python

import sys

from pexpect import pxssh
import getpass

ss=pxssh.pxssh()
host=raw_input('hostname :')
user=raw_input('username :')
port=raw_input('22222')
passw=getpass.getpass('password :')

ss.login(host,user,passw,port)
