import sys
import time
from threading import Timer

class Reader:
	def __init__(self, bufferInput = '/dev/hidraw0'):
		self.fp = open(bufferInput, 'rb')

	def parseCard(self):
		string = {'string': ''}
		def cancelString(totalString):
			totalString['string'] = ''
		timeout = Timer(2.5, cancelString, [string])
		while True:
		        buffer = self.fp.read(8)
		        for c in buffer:
		                if ord(c) > 29 and ord(c) < 41:
		                        if not timeout.isAlive():
		                                timeout = Timer(2.5, cancelString, [string])
		                                timeout.start()
		                        if ord(c) == 40:
						if timeout.isAlive():
							timeout.cancel()
		                                return string['string']
                		        else:
		                                if ord(c) == 39:
                		                        string['string'] = string['string'] + '0'
                              			else:
		                                        string['string'] = string['string'] + chr(ord(c)+19)

