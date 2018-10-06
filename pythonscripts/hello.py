#!/usr/bin/python

import sys
print "Hello Sir! Test"

print "### print ke bawah dengan while ##"
print "while statement example :"
start=1
akhir=10
chars= "#"
print start, " to " ,akhir,"\r"

while start < akhir :
    print chars
    start +=1
print '###print ke samping dengan for statement ###'
for i in xrange(0,10): print '$',
