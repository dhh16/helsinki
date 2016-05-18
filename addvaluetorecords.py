import json

import csv

import sys
import os

import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('data/pasila-records-2016-05-17.json') as data_file:
	data = json.load(data_file)

rownames = ['soft','hard']
words = {}

for rowname in rownames:
	words[rowname] = []

with open('data/pasila-subjects_korjattu.csv') as csvfile:
	reader = csv.DictReader(csvfile)
   	for row in reader:
		for rowname in rownames:
			if row[rowname] and len(row[rowname].strip())>0:
				words[rowname].append(str(row[rowname]))
				#streets.append(row['nimi'])

#streets.sort()

for street in data:
	for record in street['records']:
		value = 0
		if 'subjects' in record.keys():
			for subject in record['subjects']:
				subjectstring = subject[0].encode('utf-8')
				if subjectstring in words['soft']:
					value -= 1
				if subjectstring in words['hard']:
					value += 1
		print value
		record['value'] = value


outputfile = 'data/pasila-records-with-values.json'

with open(outputfile, 'w') as outfile:
	json.dump(data, outfile)
