#!/usr/bin/env python

#used to find sum of the values of keys generated by mapper

import sys

prevkey = None

total = 0
for input_line in sys.stdin:
	input_line = input_line.strip()
	currkey, value = input_line.split("\t", 1)
	value = int(value)
	if prevkey == currkey:
		total += value
	else:
		if prevkey:
			print( "%s\t%d" % (prevkey, total) )
		total = value
		prevkey = currkey

if prevkey == currkey:
	print( "%s\t%d" % (prevkey, total) )
