import FinnaRecords

import csv

import time

import json

import sys

streets = []

with open('data/streetnames.csv') as csvfile:
	reader = csv.DictReader(csvfile)
   	for row in reader:
		streets.append(row['nimi'])

records = []

for i in streets:
	newrecords = FinnaRecords.getFinnaRecords(i)
	streetrecords = { 'streetname' : i, 'records' : newrecords }
	records.append(streetrecords)

if not os.path.exists("data"):
	os.makedirs("data")
with open('data/streets-records.json', 'w') as outfile:
	json.dump(records, outfile)

'''for street in data:
	for record in street['records']:
		row = []
		row.append(street['name'])
		row.append(record['id'])
		with open('data/street-record.csv', 'ab') as f:
			writer = csv.writer(f)
			writer.writerow([s.encode("utf-8") for s in row])'''

