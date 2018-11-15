import sys
import time
from dbHandler import Connection
from readCardHandler import Reader
from threading import Timer

db = Connection('database/testData.db')
reader = Reader('/dev/hidraw0')

def createCard():
	string = {'string': ''}
	name = raw_input("What name should this card have?: ")
	type = raw_input("What privelage does this card have? -1 = debug 0=admin 1=user: ")
	credit = raw_input("How many credits should this card start with?: ")
	print("Scan card now")
	db.insertNew(reader.parseCard(), type, credit, name)
	answer = raw_input("Card Created, create another? y/n: ")

while True:
	if createCard() == 'n':
		sys.exit()
