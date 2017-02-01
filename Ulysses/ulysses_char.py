####################
#
# Script to write csv of characters in Ulysses with
# total number of lines in which they appear
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

