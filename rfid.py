import sys
import uinput
from dbHandler import Connection
from soundHandler import Sound
from threading import Timer

db=Connection('testData.db')
sound=Sound('./sounds/')

device = uinput.Device([
	uinput.KEY_F4
	])

fp = open('/dev/hidraw0', 'rt')

string =  ''
def cancelString(totalString):
	sound.play('reject')
	totalStringstring = ''

t=Timer(2.5, cancelString, [string])

while True:
	buffer = fp.read(8)
	for c in buffer:
		if ord(c) > 0:
			if not t.isAlive():
				t=Timer(2.5, cancelString, [string])
				t.start()
			if ord(c) == 40:
				print('submitting RFID')
				print('submission is :' + string)
				if t.is_alive():
					t.cancel()
				statusSound=db.removeCredit(string)
				print('removed credit for : ' + string)
				string = ''
			else:
				string = string + chr(ord(c))
				print(type(c))
				print('chr(ord(c))')
				print(chr(ord(c)))
				print('ord(c)')
				print((ord(c)))
				print('c')
				print(c)
			#device.emit_click(uinput.KEY_F4)
