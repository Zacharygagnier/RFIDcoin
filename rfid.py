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

fp = open('/dev/hidraw0', 'rb')

string =  ''

def cancelString(totalString):
	print(totalString)
	print('TIMER END')
	sound.play('reject')
	totalStringstring = ''
	

t=Timer(2.5, cancelString, [string])

while True:
	buffer = fp.read(8)
	for c in buffer:
		if ord(c) > 0:
			if not t.isAlive():
				print('started')
				t=Timer(2.5, cancelString, [string])
				t.start()
			print(c)
			if ord(c) == 40:
				print('submitting')
				if t.is_alive():
					t.cancel()
					print('canceled timer')
				statusSound=db.removeCredit(string)
				print('removed credit for : ' + string)
				string = ''
#			string = string + str(ord(c))
			string = string + str(c)
			#device.emit_click(uinput.KEY_F4)
#			os.system('mpg123 -q coin.mp3 &')
