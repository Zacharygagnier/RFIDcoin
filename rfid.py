import sys
import uinput
import time
import evdev
from dbHandler import Connection
from soundHandler import Sound
from readCardHandler import Reader
from config import settings
from evdev import UInput, ecodes as e

db=Connection(settings['database'])
sound=Sound('./sounds/')
read=Reader(settings['inputDevice'])
device = evdev.InputDevice(settings['outputDevice'])

sound.play('accept')
def processCard():
	tag=read.parseCard()
	print('Submitting: ' + tag)
	statusSound=db.removeCredit(tag)
	print(statusSound)
	if statusSound == 'accept':
		print('Accepted credit for: ' + tag)
               	device.write(e.EV_KEY, getattr(e, settings['keyPress']), 1)
		time.sleep(.3)
		device.write(e.EV_KEY, getattr(e, settings['keyPress']), 0)
	sound.play(statusSound)

while True:
	processCard()
