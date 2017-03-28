# Use the command python q2.py to run the program

from re import match
#---------------------------------------------------------------------------------------------

def find_product(z):
    
    myRanges = map(lambda x: (x, x + 5), xrange(len(z) - 4))
    print "myRanges is {}".format(myRanges)

    mySlices = map(lambda x: (x[0], list(z[x[0]:x[1]])), myRanges)
    print "mySlices is {}".format(mySlices)

    myList = map(lambda x: (x[0], reduce(lambda a,b: a*b, x[1])), mySlices)
    print "myList is {}".format(myList)

    #print myList[0][1]
    return reduce(maxTuple, myList)

#---------------------------------------------------------------------------------------------

def maxTuple(a,b):
    return (a[1] > b[1] and a) or (b[1] > a[1] and b)

#---------------------------------------------------------------------------------------------

#Example program as given in handout
z = [1, 2, 3, 4, 5, 6, 4, 2, 1, 3]
print find_product(z)

#---------------------------------------------------------------------------------------------
