import json

import csv

import sys

import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('data/streets-records-2016-05-16.json') as data_file:
	data = json.load(data_file)

uniquefields = []

for street in data:
        for record in street['records']:
		for key in record.keys():
			if key not in uniquefields:
				uniquefields.append(key)

uniquefields.sort()

row = []
row.append('streetname')
for s in uniquefields:
	row.append(s.encode("utf-8"))
with open('data/records.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(row)

for street in data:
        for record in street['records']:
        	row = []
		row.append(street['streetname'])
		for field in uniquefields:
			if field in record.keys():
				if isinstance(record[field], (list, dict)):
					subfields = []
					for subfield in record[field]:
						if isinstance(subfield, (dict)):
							for subsubfield in subfield.items():
								subfields.append(':'.join(subsubfield))
						else:
							subfields.append(''.join(subfield))
					#row.append(','.join(record[field].values()))
                			row.append(','.join(subfields))
				#elif isinstance(record[field], dict):
				#	subfields = []
				#	for subfield in record[field]:
				#		subfields.append(','.join(subfield.values()))
                		#	row.append(','.join(subfields))
				else:
                			row.append(record[field])
			else:
				row.append('')
                with open('data/records.csv', 'ab') as f:
                        writer = csv.writer(f)
                        writer.writerow([s.encode("utf-8") for s in row])

