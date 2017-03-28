class wordIterator:
	def __init__(self, fileName):
		self.words = []
		self.f = open(fileName, "r")


	def __iter__(self):
		return self

	def next(self):
		if len(self.words) > 0:
			return self.words.pop(0)
		else:	
			newLine = self.f.next()
			if newLine == '':
				raise StopIteration
			else:
				self.words = newLine.split()
				return self.words.pop(0)

	
myObject = wordIterator("test.txt")
#iter(myObject)
for word in myObject:
	print word
