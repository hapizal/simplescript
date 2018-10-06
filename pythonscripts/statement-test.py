#!/usr/bin/python 
import sys

print "while statement example :"
start=1
akhir=10
chars= "#"
print start, " to " ,akhir,"\r"

while start < akhir : print chars ; start +=1
print '###print ke samping dengan for statement ###'
n = input("How many char :")
kar = raw_input("what char?:")
for i in xrange(0,n): print (kar),
print "\r"
for i in xrange(0,n):sys.stdout.write(kar); sys.stdout.flush()
print "\r"
