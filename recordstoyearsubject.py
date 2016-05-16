import json

import csv

import sys

import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('data/streets-records-2016-05-16.json') as data_file:
	data = json.load(data_file)

outputfile = 'data/yearsubject.json'

years = []

for street in data[0:5]:
        for record in street['records']:
		if 'year' in record.keys():
			year = record['year']
			if year not in years:
				years.append(year)

years.sort()

yearsubject = {}

for year in years:
	subjects = {}
	for street in data:
		for record in street['records']:
			if 'year' in record.keys() and 'subjects' in record.keys():
				if year == record['year']:
					for subject in record['subjects']:
						subjectstring = str(subject)
						if subjectstring in subjects.keys():
							subjects[subjectstring] += 1
						else:
							subjects[subjectstring] = 1
	#subjects.sort()
	print subjects
