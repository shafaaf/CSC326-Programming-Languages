# Run python q5.py to run the program
# For this question, make sure that the file with the short text is named as q5Test.txt
# This code will parse the file q5Test.txt

import re
#---------------------------------------------------------------------------------------------

def split_sentence(myFile):
	with open(myFile, 'r+') as f:
		read_data = f.read()
		print "Original sentence: "
		print read_data
		print ("\n")

		text = read_data.replace('\n', ' ').replace('\r', '')
		m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
		myNewSentence = []
		print "New sentence:"
		for i in m:
	         myNewSentence.append(i)
	         print i  
		return myNewSentence 

#---------------------------------------------------------------------------------------------

#Example program
newSentence = []
newSentence = split_sentence("q5Test.txt")
print "\n"
print "New sentence:"
for i in newSentence:
	print i
