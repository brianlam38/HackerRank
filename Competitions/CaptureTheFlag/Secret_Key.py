# Extract information from a given website and submit the specified output as Plain Text.
# https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/

import requests

URL = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json"

response = requests.get(URL)		# GET request to fetch response
keys = response.json()				# Parse data to json formats
print keys

# GET request loop for each key-value pair
#i = 0
#for value in key_value.text[i]:
	# grab key string
#	print value
#	i += 1

	#key_value = requests.get("https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json")
	#https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/mars.json



