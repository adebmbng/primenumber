#!bin/python

import sys
import time

import asyncio


answer = False

async def prime(initNumber, totalThreads, mValue):
	x=0
	while True:
		global answer
		if(answer):
			# print("--- %s seconds ---" % (time.time() - start_time))
			sys.exit()
		modCalculation = (initNumber+(totalThreads * x))
		# print("%s mod %s = %s ---- %s init " % (mValue, modCalculation,(mValue % modCalculation), self.initNumber))
		if modCalculation < 3:
			x+=1
		elif modCalculation < mValue:
			if (mValue % modCalculation) == 0:
				elapsed = time.perf_counter() - s
				print (f"Input isn't prime number ({modCalculation})(on Thread {initNumber}) -----{elapsed:0.10f} seconds.-----" )
				# print ("--- %s seconds ---" % (time.time() - start_time))
				answer=True
				sys.exit()
				break
			else:
				x += 1
		else:
			break

async def main():
    # await asyncio.gather(prime(1, 5, 1223), prime(2, 5, 1223), prime(3, 5, 1223), prime(4, 5, 1223), prime(5, 5, 1223))
    # await asyncio.gather(prime(1, 2, 1003), prime(2, 2, 1003))
    await asyncio.gather(prime(1, 10, 1003), prime(2, 10, 1003), prime(3, 10, 1003), prime(4, 10, 1003), prime(5, 10, 1003), prime(6, 10, 1003), prime(7, 10, 1003), prime(8, 10, 1003), prime(9, 10, 1003), prime(10, 10, 1003))
    # await asyncio.gather(prime(1, 1, 1003))

if __name__ == "__main__":
    s = time.perf_counter()
    start_time = time.time()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print (f"-----{elapsed:0.10f} seconds.-----" )



