#!bin/python

import sys
import argparse
import time
import threading


totalThreads = 1
mValue = 1
inputNumber = 1

answer = False

class primeThread(threading.Thread):
	def __init__(self, initNumber, totalThreads):
		threading.Thread.__init__(self)
		self.initNumber = initNumber
		self.totalThreads = totalThreads
		
	def run(self):
		x = 0
		while True:
			global answer
			if(answer):
				# print("--- %s seconds ---" % (time.time() - start_time))
				sys.exit()
			modCalculation = (self.initNumber+(self.totalThreads * x))
			# print("%s mod %s = %s ---- %s init " % (mValue, modCalculation,(mValue % modCalculation), self.initNumber))
			if modCalculation < 3:
				x+=1
			elif modCalculation < mValue:
				if (mValue % modCalculation) == 0:
					print "Input isn't prime number (%s)(on Thread %s) --- %s seconds ---" % (modCalculation, self.initNumber, (time.time() - start_time))
					# elapsed = time.perf_counter() - s
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
	start_time = time.time()
	mValue = args.input
	totalThreads = args.threads

	if mValue <= 3:
		print "Input is prime number"
	else:
		prime = True
		procs = []
		print("total thread: %s" % args.threads)
		for x in range(1, args.threads+1):
			print("starting thread %s --- %s seconds ---" % (x,(time.time() - start_time)))
			t = primeThread(x, totalThreads)
			t.daemon = True
			t.start()
			# procs.append(t)
			# t.start()
			# t.is_alive()
			# t.join()
		# for proc in procs:
		# 	proc.join()

