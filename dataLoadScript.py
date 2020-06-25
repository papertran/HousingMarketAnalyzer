import sys
import os
import sqlite3
# Usage - python3 dataLoadScript.py <filename>
# This does not error check. assumes folder contains only files with correct format

if len(sys.argv) == 1:
	print("Error wrong usage, needs 1 argument")
	exit(1)

# constants to use
months = ["4", "5", "6", "7", "8", "9", "10", "11", "12", "1", "2", "3"]
year = 2010
# Variable setup
lines = []

print(os.listdir(sys.argv[1]))

# Load all files from a directory
for filename in os.listdir(sys.argv[1]):
	with open(os.path.join(sys.argv[1], filename), 'r') as file:
		data = file.readlines()
		for line in data[3:]:
			lines.append(line.strip())

# print(lines[0])
print(lines[0])

# # Remember to ignore the first 3 lines
# print(lines[0])

# for house in lines[3:4]:
# 	houseVariables = house.split(',')
# 	# Insert into the data_house the house
# 	print(houseVariables[0:4])