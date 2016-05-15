import lxml.etree

import requests
import requests_cache

import json

import time

import sys

import urllib

import os

import pprint
pp = pprint.PrettyPrinter(indent=4)

def getFinnaRecords(lookfor):
	resultlimit = 100
	sleeptime = 3
	searchfilter = "~usage_rights_str_mv%3A\"usage_B\""
	page = 1
	query = "https://api.finna.fi/v1/search?lookfor={0}&type=AllFields&limit={1}&filter[]={2}&page={3}"

	response_dict = []

	allfromcache = True

	sys.stdout.write("getting records for " + lookfor)
	sys.stdout.flush()
	while True:
		url = query.format(urllib.quote(lookfor), resultlimit, searchfilter, page)
		response = requests.get(url)
		response_dict.append(response.json())
		sys.stdout.write('.')
		sys.stdout.flush()
		if not response.from_cache:
			time.sleep(sleeptime)
			allfromcache = False
		resultnumber = response_dict[0]['resultCount']
		page += 1

		if page * resultlimit > resultnumber:
			sys.stdout.write('\n')
			break

	if not allfromcache:
		time.sleep(sleeptime)
	images = []
	for response in response_dict:
		if int(response['resultCount']) > 0:
			return response['records']
		else:
			return []


if not os.path.exists("data"):
	os.makedirs("data")

requests_cache.install_cache('data/finna_cache', backend='sqlite')

'''searchterm = str(sys.argv[1])

records = getFinnaRecords(searchterm)

pp.pprint(records)'''

#with open('data/' + searchterm + '.json', 'w') as outfile:
#	json.dump(records, outfile)
