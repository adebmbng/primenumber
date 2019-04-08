#!bin/python

import sys
import argparse
import time
import multiprocessing


totalThreads = 1
mValue = 1
inputNumber = 1

answer = False

def primeFinder(mInit, mThread):
	x = 0
	while True:
		global answer
		if(answer):
			# print("--- %s seconds ---" % (time.time() - start_time))
			sys.exit()
		modCalculation = (mInit+(mThread * x))
		# print("%s mod %s = %s ---- %s init " % (mValue, modCalculation,(mValue % modCalculation), mInit))
		if modCalculation < 3:
			x+=1
		elif modCalculation < mValue:
			if (mValue % modCalculation) == 0:
				print "Input isn't prime number (%s)(on Thread %s) --- %s seconds ---" % (modCalculation, mInit, (time.time() - start_time))
				# print ("--- %s seconds ---" % (time.time() - start_time))
				answer=True
				sys.exit()
				break
			else:
				x += 1
		else:
			break


parser = argparse.ArgumentParser()
parser.add_argument("input", help="input any number",
                    type=int)
parser.add_argument("threads", help="input total thread",
                    type=int)
args = parser.parse_args()

if args.input:
	mValue = args.input
	totalThreads = args.threads
	start_time = time.time()
	if mValue <= 3:
		print "Input is prime number"
	else:
		prime = True
		print("total thread: %s" % args.threads)
		procs = []
		for x in range(1, args.threads+1):
			print("starting thread %s --- %s seconds ---" % (x,(time.time() - start_time)))
			p = multiprocessing.Process(target=primeFinder, args=(x, totalThreads))
    		# procs.append(p)
    		p.start()
    	# for proc in procs:
     #    	proc.join()

