#!usr/bin/python

import sys

def local_func():
	print "execute local_func"

if __name__ == "__main__":  
	local_func()
	print "execute global"