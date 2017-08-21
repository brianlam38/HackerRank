# Extract information from a given website and submit the specified output as Plain Text.
# https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/

import requests

key_url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json"
response = requests.get(key_url)			# GET request to fetch response
keys = response.json()						# Parse data to .json
print keys

val_url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/"
#keylen = len(keys)
val_list = []

for key in keys:										# loop through json object to grab each key
	response = requests.get(val_url + key + ".json")	# GET request to fetch value using key
	value = response.json()
	str_value = value['news_title']
	print str_value
	val_list.append(str_value)							# append value to list

val_list.sort()											# sort list
text_file = open("Output.txt", "w")						# create output .txt file
for item in val_list:									# write output to .txt file
	text = str(item)
	text_file.write(text + "\n")
text_file.close()





