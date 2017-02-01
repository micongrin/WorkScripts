####################
#
# Script to sort characters in Ulysses in order 
# of total number of lines in which they appear
#
####################

import csv
characters = {}
lines = int()
fieldnames = ['character', 'linein', 'lineout']
with open('/Users/connerms/Downloads/ulysses2.csv', 'rb') as mentions:
	reader = csv.DictReader(mentions, fieldnames=fieldnames)
	for row in reader:
		character = row['character']
		if not row['lineout']:
			lines = 1
		else:
			lines = int(row['lineout']) - int(row['linein'])
		if character in characters:
			characters[character] = characters[character] + lines
		else:
			characters[character] = lines

with open('/Users/connerms/Downloads/freq.csv', 'w') as freq:
	newnames = ['character', 'lines']
	writer = csv.DictWriter(freq, fieldnames=newnames)
	writer.writeheader()
	for k, v in characters.iteritems():
		writer.writerow({'character': k, 'lines': v})




array of char:lines
load the csv

#count lines 
if lineout is NULL, lines is 1
if lineout is !NULL, lines is lineout-linein

#add to array
if char=character
	add lines to char:lines
else add char
	add lines to char:lines

