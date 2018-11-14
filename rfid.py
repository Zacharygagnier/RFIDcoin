import sys
import uinput
import time
import evdev
from dbHandler import Connection
from soundHandler import Sound
from threading import Timer
from evdev import UInput, ecodes as e

db=Connection('testData.db')
sound=Sound('./sounds/')



device = evdev.InputDevice('/dev/input/event3') #CHANGE IF NOT RESPONDING ON SPECIFIC INPUT
fp = open('/dev/hidraw0', 'rb') #CHANGE IF NOT READING INPUT

ui = UInput()


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
               				device.write(e.EV_KEY, e.BTN_SELECT, 1)  # CHANGE BUTTON HERE  e.BTN_WHATEVER
			                device.write(e.EV_KEY, e.BTN_SELECT, 0)  # CHANGE BUTTON HERE TOO
				sound.play(statusSound)
				string['string'] = ''
				print('removed credit for: ' + string['string'])
			else:
				string['string'] = string['string'] + chr(ord(c)+19)
