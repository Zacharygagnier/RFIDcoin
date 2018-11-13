import sys
import uinput
import time
from dbHandler import Connection
from soundHandler import Sound
from threading import Timer
from evdev import UInput, ecodes as e

db=Connection('testData.db')
sound=Sound('./sounds/')

device = uinput.Device([uinput.KEY_Q])
ui = UInput()

def hold(key):
	ui.write(e.EV_KEY, key, 1)
	ui.syn()
	return 0

def release(key):
	ui.write(e.EV_KEY, key, 0)
	ui.syn()
	return 0

fp = open('/dev/hidraw0', 'rb')

string = {'string': ''}

def cancelString(totalString):
	sound.play('reject')
	print(totalString['string'])
	totalString['string']  = ''

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
				print('submission is :' + string['string'])
				if t.is_alive():
					t.cancel()
				statusSound=db.removeCredit(string['string'])
				if statusSound == 'accept':
					hold(e.KEY_Q)
					time.sleep(1)
					release(e.KEY_Q)
				sound.play(statusSound)
				string['string'] = ''
				print('removed credit for: ' + string['string'])
			else:
				string['string'] = string['string'] + chr(ord(c)+19)
