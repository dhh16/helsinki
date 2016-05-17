import json

import csv

import sys
import os

import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('data/pasila-records-2016-05-17.json') as data_file:
	data = json.load(data_file)

outputfile = 'data/slideshow.csv'

years = []

outputfile = 'data/test.csv'

for street in data:
	for record in street['records']:
		if 'year' in record.keys():
			year = record['year']
			if year not in years:
				years.append(year)

years.sort()

'''print years'''

photos = []


'''go through years
	go through records
		if year == record year:
			append'''

for year in years:
	for street in data:
		for record in street['records']:
			if 'year' in record.keys() and record['year'] == year:
				'''print record['images']
				print record['year']'''
				for image in record['images']:
					photos.append('https://api.finna.fi' + image)

print len(photos)


'''yearsubject = {}

for year in years:
	subjects = {}
	for street in data:
		for record in street['records']:
			if 'year' in record.keys() and 'subjects' in record.keys():
				if year == record['year']:
					for subject in record['subjects']:
						subjectstring = subject[0]
						if subjectstring in subjects.keys():
							subjects[subjectstring] += 1
						else:
							subjects[subjectstring] = 1
	yearsubject[year] = subjects
'''

'''print yearsubject'''
'''

if not os.path.exists("data"):
	os.makedirs("data")
row = ['year','word','frequency']
with open(outputfile, 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(row)
for year, subjects in yearsubject.iteritems():
	for subject, frequency in subjects.iteritems():
		row = []
		row.append(year)
		row.append(subject.encode("utf-8") )
		row.append(frequency)
		with open(outputfile, 'ab') as f:
			writer = csv.writer(f)
			writer.writerow(row)
'''
