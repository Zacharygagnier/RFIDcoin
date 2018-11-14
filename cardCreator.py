import sys
import time
from dbHandler import Connection
from threading import Timer

db=Connection('testData.db')
fp = open('/dev/hidraw0', 'rb') #CHANGE IF NOT READING INPUT


def createCard():
	string = {'string': ''}
	name = raw_input("What name should this card have?: ")
	type = raw_input("What privelage does this card have? -1 = debug 0=admin 1=user: ")
	credit = raw_input("How many credits should this card start with?")
	print("Scan card now")

	def cancelString(totalString):
	        sound.play('reject')
	        print(totalString['string'])
	        totalString['string']  = ''

	t=Timer(2.5, cancelString, [string])


	while True:
	        buffer = fp.read(8)
	        for c in buffer:
	                if ord(c) > 29 and ord(c) < 41:
	                        if not t.isAlive():
	                                t=Timer(2.5, cancelString, [string])
	                                t.start()
        	                if ord(c) == 40:
	                                db.insertNew(string['string'], type, credit, name)
					answer = raw_input("Card Created, create another? y/n")
					if answer == "y":
						createCard()
					else:
						sys.exit()
                       		else:
                            	 	if ord(c) == 39:
                                        	string['string'] = string['string'] + '0'
                                	else:
                                        	string['string'] = string['string'] + chr(ord(c)+19)

createCard()
