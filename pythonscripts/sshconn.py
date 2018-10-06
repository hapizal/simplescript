#!/usr/bin/python

import sys
import pexpect

### read input
ip=sys.argv[1]

conn=pexpect.spawn('ssh -p 22222 yniptv@%s'%ip)

### Attempt to ssh
try :
    conn.expect('assword:', timeout=10)
    conn.sendline('Yniptv@Telkom147')
### send specific command after logged in
    conn.expect('~>')
    conn.sendline('uname -a')
### capture output of command
    conn.expect('>')
    print(conn.before)
############################
### exit
    conn.sendline('exit')
    conn.eof
    #conn.interact()
### if timeout exceeded, send alert or message
except pexpect.TIMEOUT:
    print "XXXXX Target OFFLINE XXXXX"
