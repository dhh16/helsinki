import requests
import requests_cache
import urllib

import time
import csv

import json

import sys
import os

if not os.path.exists("data"):
	os.makedirs("data")

streets = []

with open('data/streetnames.csv') as csvfile:
	reader = csv.DictReader(csvfile)
   	for row in reader:
		streets.append(row['nimi'])

streets.sort()

requests_cache.install_cache('data/nominatim_cache', backend='sqlite')

coordinates = []

for i in streets:

	query = "http://nominatim.openstreetmap.org/search.php?q={0}+helsinki&format=json"

	response_dict = []

	print("getting coordinates for " + i)
	url = query.format(urllib.quote(i))
	response = requests.get(url)
	response_dict.append(response.json())
	if not response.from_cache:
		time.sleep(1)

	if response_dict[0]:
		lon = response_dict[0][0]['lon']
		lat = response_dict[0][0]['lat']
		coords = lat + ',' + lon
	else:
		coords = "NA"

	location = {'streetname' : i, 'coordinates' : coords}

	coordinates.append(location)

row = ['streetname','latlong']
with open('data/street-coordinates.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(row)
for street in coordinates:
	row = []
	row.append(street['streetname'])
	row.append(street['coordinates'])
	with open('data/street-coordinates.csv', 'ab') as f:
		writer = csv.writer(f)
		writer.writerow(row)

