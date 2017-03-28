# Run python q4.py to run the program
# This code will parse the file q4Test.txt

import operator
#---------------------------------------------------------------------------------------------

class myWordIterator:
	def __init__ (self, myFile):
		self.i = 0
		self.f = open(myFile, 'r')
		self.words = []

	def __iter__(self):
		return self

	def next(self):

		if len(self.words) > 0:
			return self.words.pop(0)
	
		else: #what if get exception here
			nextLine = self.f.next()
			self.words = nextLine.split()
			return self.next()

#---------------------------------------------------------------------------------------------

def find_popular(myFile):
	popularWords = {}
	it = myWordIterator(myFile)
	for word in it:
		#print word
		if(word in popularWords):
			popularWords[word] = popularWords[word] + 1
		else:
			popularWords[word] = 1			

	sortedByValue = sorted(popularWords.items(), reverse = True, key=operator.itemgetter(1))
	#print "All values are:\n {}".format(sortedByValue)

	top10List = []
	top10List = sortedByValue[:10]

	print "Top 10 most popular words are: "
	for element in top10List:
		print element[0]

#---------------------------------------------------------------------------------------------

#Example program
find_popular("q4Test.txt")
