import sys
import os
import sqlite3
import csv
# Usage - python3 dataLoadScript.py <filename>
# This does not error check. assumes folder contains only files with correct format

if len(sys.argv) == 1:
	print("Error wrong usage, needs 1 argument")
	exit(1)

# constants to use
months = ["4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3"]

# Variable setup
lines = []
year = 2010
con = sqlite3.connect('db.sqlite3')
# SQL Statements


# print(os.listdir(sys.argv[1]))

# Load all files from a directory
for filename in os.listdir(sys.argv[1]):
	with open(os.path.join(sys.argv[1], filename), 'r') as file:
		# data = file.readlines()
		spamreader = csv.reader(file, delimiter=',')
		skipLines = 0
		for row in spamreader:
			skipLines += 1
			if skipLines < 3:
				continue
			lines.append(row)


# print(lines[0])
# print(lines[0])
# print(len(lines))

inserVal = 1
for house in lines:
	# some houses have no data in the price, then skip those
	if house[3] == '':
		continue

	# To show that stuff is inserting
	if inserVal % 100 == 0:
		print("Inserted {} entries".format(inserVal))
	inserVal += 1

	houseInsert ="insert into data_house (region, HouseType) Values ('{}', '{}');".format(house[0], house[2])
	
	# Insert into the House table
	try:
		con.execute(houseInsert)
	except Exception as e:
		print("error: ", end='')
		print(e)
	con.commit()

	# Get the house id 
	findHouseId = "SELECT id FROM data_house WHERE region = '{}' AND HouseType = '{}'".format(house[0], house[2])
	cur = con.cursor()
	cur.execute(findHouseId)
	try:
		houseId = cur.fetchone()[0]
	except Exception as e:
			print("error house id not found: ", end='')
			print(e)
			continue
	# print(houseId)


	# Insert into the Price Table
	counter = 0
	dateFormat = "{}-{}-15"
	for value in house[3:]:
		priceInsert = "INSERT INTO data_price (listingDate, Price, houseId_id, Predicted) VALUES ('{}', '{}', '{}', False)"
		cleanedValue = int(value.replace(',', '').replace('$', ''))
		date = dateFormat.format(year, months[counter])
		# Set the next month and check if the next month is in the new year
		if counter == 8:
			year += 1
		if counter ==  11:
			counter = 0
		else:
			counter += 1
		
		try:
			con.execute(priceInsert.format(date, cleanedValue, houseId))
		except Exception as e:
			print("error: ", end='')
			print(e)
		
	year = 2010
	con.commit()


con.close