def my_reduce(myFunc, myIterable, initializer = None):
    myIterable = iter(myIterable)
    try:
        x = myIterable.next() if initializer is None else initializer
        print "x is {0}".format(x)
    except StopIteration:
        raise TypeError("got error")
    for i in myIterable:
    	print "Now: x is {0}, i is {1}".format(x, i)
        x = myFunc(x, i)
        print "Now: x is {0}".format(x)
    return x


def add (x,y):
	return x+y

l1 = [1,2,3,4]
print my_reduce(add, l1)


print "normal reduce:"
print reduce(add, l1)


