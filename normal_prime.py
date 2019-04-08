#!bin/python

import sys
import argparse
import time

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input any number",
                    type=int)
args = parser.parse_args()

if args.input:
	mValue = args.input
	if mValue <= 3:
		print "Input is prime number"
	else:
		prime = True
		for x in range(2, (mValue-1)):
			if (mValue % x) == 0:
				prime = False
				break
		if prime:
			print "Input is prime number"
		else:
			print "Input isn't prime number"

		print("--- %s seconds ---" % (time.time() - start_time))

