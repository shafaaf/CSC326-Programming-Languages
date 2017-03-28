# Run python q1.py to run the program
# The example program - calls foo() 3 times, calls bar() 2 times, and then prints PROFILE_RESULTS

from time import clock
import time
#---------------------------------------------------------------------------------------------

PROFILE_FUNCTIONS = True
PROFILE_RESULTS = {}

#---------------------------------------------------------------------------------------------

def profile(func):
	def func_wrapper(*args, **kargs):

		if PROFILE_FUNCTIONS:
			#print "Timing needed."
			start = clock()
			func(*args, **kargs)
			functionDuration = clock() - start
			#print('The function took {} seconds'.format(functionDuration))

			funcName = func.__name__
			#print "The function name is {0}".format(funcName)

			if funcName in PROFILE_RESULTS:
				#print "{0} IN PROFILE_RESULTS".format(funcName)
				oldTuple = PROFILE_RESULTS[funcName]
				oldDurationAvg = oldTuple[0]
				oldCalls = oldTuple[1]

				totalDuration = (oldDurationAvg * oldCalls) + functionDuration
				newCalls = oldCalls + 1
				newDurationAvg = totalDuration/newCalls
				
				newTupleValue = (newDurationAvg, newCalls)
				PROFILE_RESULTS[funcName] = newTupleValue

			else:
				#print "{0} NOT in PROFILE_RESULTS".format(funcName)
				calls = 1
				tupleValue = (functionDuration, calls)
				PROFILE_RESULTS[funcName] = tupleValue

			#print("Finished adding")
			print "PROFILE_RESULTS after adding current one is now: {0}\n".format(PROFILE_RESULTS)
			return

		else:
			#print "Sorry, no timing needed. Run function normally."
			func(*args, **kargs)
			return

	return func_wrapper

#---------------------------------------------------------------------------------------------

@profile
def foo(n):
	for i in range(0,n):
		for j in range(0,n/2):
			x = i + j
			print "x is {0}".format(x)
	return

@profile
def bar():
	x = 0
	for i in range(0,200000):
		x = x + i
	#print "x is {0}".format(x)
	return

#---------------------------------------------------------------------------------------------
	
#Example program - calls foo() 3 times, calls bar() 2 times, and then prints PROFILE_RESULTS
foo(5)


print "Final output will be printed below: "
print "Final PROFILE_RESULTS is: {0}".format(PROFILE_RESULTS)

