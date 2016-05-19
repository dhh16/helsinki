import json

import csv

import sys
import os

import urllib
import time

import math
import re

import subprocess
from subprocess import call


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

photos = []


if not os.path.exists("images"):
	os.makedirs("images")
if not os.path.exists("images/original"):
	os.makedirs("images/original")
if not os.path.exists("images/processed"):
	os.makedirs("images/processed")

n=0

for year in years:
        	for street in data:
                	for record in street['records']:
                        	if 'year' in record.keys() and record['year'] == year:
                                	for image in record['images']:
						'''if file doesnt exist yet:'''
						if not os.path.isfile("images/original/" + record['id'] + ".jpg"):
							time.sleep(1)
							urllib.urlretrieve ("https://api.finna.fi/Cover/Show?id=" + urllib.quote(record['id']) + "&fullres=1&index=0", "images/original/" + record['id'] + ".jpg")
							'''print("https://api.finna.fi/Cover/Show?id=" + urllib.quote(record['id']) + "&fullres=1&index=0")'''
						'''if the copy of the file with embedded text doesn't exist yet'''
						if not os.path.isfile("images/processed" + record['id'] + ".jpg"):

							if 'nonPresenterAuthors' in record:
								for authorinfo in record['nonPresenterAuthors']:
									author = authorinfo['name']
									if(author == "Tuntematon"):
										author = "unknown"
							else:
								author = "unknown"
							subjects = ""
							if 'subjects' in record:
								for subject in record['subjects']:
									subjects = subjects + "\n" + subject[0]
							subprocess.call("convert images/original/" + record['id'] + ".jpg -fill white  -undercolor '#00000080'  -gravity Southeast -annotate +5+5 'Year: " + year + "\nAuthor: " + author + "' images/processed/"  + record['id'] + ".jpg", shell=True)
							subprocess.call("convert images/processed/" + record['id'] + ".jpg -fill white  -undercolor '#00000080'  -gravity West -annotate +5+0 '" + subjects + "' images/processed/"  + record['id'] + ".jpg", shell=True)


							value = record['value']
							valuesize = 30 + (10 * abs(value))
							if valuesize == 0:
								valuesize = 30
							if value < 0:
								valuecolor = "'#FF4C4C'"
							elif value == 0:
								valuecolor = "white"
							elif value > 0:
								valuecolor = "'#00FF00'"
							value = str(value)
							subprocess.call("convert images/processed/" + record['id'] + ".jpg -fill " + valuecolor + "  -undercolor '#00000080' -pointsize " + str(valuesize) + " -gravity North -annotate +5+0 '" + value + "' images/processed/"  + record['id'] + ".jpg", shell=True)

		n = n+1
		completed = (100 * n / len(years))
		print (str(completed) + "% completed")
	
						




'''print len(photos)'''


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
