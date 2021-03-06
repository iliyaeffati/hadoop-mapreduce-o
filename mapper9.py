#!/usr/bin/python

'''
Create an inverted index of the words found in the body of each node of the forum, 
i.e. index word, nodeid_1, nodeid_2, ...
Work on data from the udacity forum (similar to Stack Exchange format). 
The dataset for this mapper was generated by exporting data from a SQL database.

The data in at least one of the fields (the body field) can include newline
characters, and all the fields are enclosed in double quotes. Therefore, we
will need to process the data file in a way other than using split(","). To do this, 
we have provided sample code for using the csv module of Python. Each 'line'
will be a list that contains each field in sequential order.
 
In this exercise, we are interested in the field 'body' (which is the 5th field, 
line[4]).

Mapper returns (word, node_id) pairs for each word in the body of each entry. 
'''

import sys, csv

reader = csv.reader(sys.stdin, delimiter='\t')
noNoList = ['.',',','!','?',':',';','\"','(',')','<','>','[',']','#','$','=','-','/']

for line in reader:
	if line[0]=="id":
		continue
	elif len(line) == 19:
		nodeid = line[0]
		body = line[4]
	for ch in noNoList:
		body = body.replace(ch," ")
	body = body.replace("  "," ")
	wordlist = body.lower().split(" ")
	for word in wordlist:   
		print "{0}\t{1}".format(word, nodeid)

