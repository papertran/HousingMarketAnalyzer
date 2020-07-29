import sys
import os
import sqlite3
import csv
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Usage - python3 dataLoadScript.py <filename>
# This does not error check. assumes folder contains only files with correct format

if len(sys.argv) == 1:
	print("Error wrong usage, needs 1 argument")
	exit(1)

# constants to use
months = ['4', '5', '6', '7', '8' ,'9']

# Variable setup
lines = []
year = 2020
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
			# print(row)

# print(lines)
# print(lines[0])
# print(lines[0])
# print(len(lines))

inserVal = 1
for house in lines:
	# some houses have no data in the price, then skip those
	if house[3] == '':
		continue

	# Show stuff in inserting
	if inserVal % 100 == 0:
		print("Inserted {} entries".format(inserVal))

	inserVal += 1

	# Get the house id 
	findHouseId = "SELECT id FROM data_house WHERE region = '{}' AND HouseType = '{}'".format(house[0], house[2])
	cur = con.cursor()
	cur.execute(findHouseId)
	try:
		houseId = cur.fetchone()[0]
	except Exception as e:
			# print("error house id not found: ", end='')
			# print( "region = '{}' AND HouseType = '{}'".format(house[0], house[2]))
			continue
	# print(houseId)

	
	findLastDate = "SELECT listingDate FROM data_price WHERE houseId_id = '{}' ORDER BY listingDate DESC".format(houseId)
	cur.execute(findLastDate)
	lastDate = cur.fetchone()[0]
	lastDate = datetime.strptime( lastDate, "%Y-%m-%d")

	# Get 6 months after last date
	dateArray = []
	for i in range(6):
		increment =  relativedelta(months=+1)
		lastDate = lastDate + increment
		dateArray.append(lastDate)
	
	# Insert into the Price Table
	counter = 0
	dateFormat = "{}-{}-15"
	for value in house[3:]:
		# print(value)
		priceInsert = "INSERT INTO data_price (listingDate, Price, houseId_id, Predicted) VALUES ('{}', '{}', '{}', True)"
		cleanedValue = math.floor(float(value))
		date = dateArray[counter].date()
		counter += 1

		try:
			con.execute(priceInsert.format(date, cleanedValue, houseId))
		except Exception as e:
			print("error: ", end='')
			print(e)
		
	con.commit()

con.close