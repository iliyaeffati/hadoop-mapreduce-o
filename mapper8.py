#!/usr/bin/python
"""
Print out 10 lines containing longest posts, sorted in ascending order from shortest to 
longest. This is a "Top-N" MapReduce pattern.
Work on data from the udacity forum (similar to Stack Exchange format). 
The dataset for this mapper was generated by exporting data from a SQL database.

The data in at least one of the fields (the body field) can include newline
characters, and all the fields are enclosed in double quotes. Therefore, we
will need to process the data file in a way other than using split(","). To do this, 
we have provided sample code for using the csv module of Python. Each 'line'
will be a list that contains each field in sequential order.
 
In this exercise, we are interested in the field 'body' (which is the 5th field, 
line[4]).
"""

import sys
import csv
import time

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	topTen = []

	for line in reader:
		currentBody = line[4]
		currentLength = len(currentBody)
		inserted = False
		for i,ln in enumerate(topTen):
			if currentLength>len(ln[4]):
				topTen.insert(i,line)
				inserted = True
				break
		if not inserted and len(topTen)<10:
			topTen.insert(len(topTen)+1,line)

		if len(topTen)>10:
			topTen.pop()

	topTen.reverse()    
	for line in topTen:
		writer.writerow(line)

test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

main()

