import os


company = input("Input company name: ")
position = input("Input position name: ")

with open('coverletter.txt', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('[cpy]', company)	
filedata = filedata.replace('[pos]', position)

with open('coverletter.txt', 'w') as file:
	file.write(filedata)

	