from time import clock

PROFILE_FUNCTIONS = True
PROFILE_RESULTS = {}

def myDecorator(some_function):
	def wrapper(*args, **kwargs):

		if PROFILE_FUNCTIONS:
			print "Will record time"
			start = clock()
			some_function(*args, **kwargs)
			duration = clock() - start
			print "Duration is {}".format(duration)
			funcName = some_function.__name__
			#print ("Function name is: {}".format(funcName))

			if funcName in PROFILE_RESULTS:
				print "{} ALREADY in PROFILE_RESULTS".format(funcName)
				
				oldTuple = PROFILE_RESULTS[funcName]
				oldFullRunTime = oldTuple[0] * oldTuple[1]
				newFullRunTime = oldFullRunTime + duration
				newNumCalls = oldTuple[1] + 1
				newAvgRuntime = newFullRunTime/newNumCalls
				newTuple = (newAvgRuntime,newNumCalls)
				PROFILE_RESULTS[funcName] = newTuple

			else:
				print "{} NOT in PROFILE_RESULTS".format(funcName)
				avgRunTime = duration
				numCalls = 1
				myTuple = (avgRunTime, numCalls)
				PROFILE_RESULTS[funcName] = myTuple

		else:
			print "Will NOT record time"
			some_function(*args, **kwargs)

		print "PROFILE_RESULTS is now: {}\n".format(PROFILE_RESULTS)

	return wrapper


@myDecorator
def foo(x):
	sum = 0
	for i in range(0,x):
		sum += i
	print "foo: sum is: {}".format(sum)
	return

@myDecorator
def bar(x):
	sum = 0
	for i in range(0,x):
		sum += i
	print "bar: sum is: {}".format(sum)
	return


foo(5000000)
foo(1000000)
bar(30000000)
bar(6000000)
bar(8900045)






