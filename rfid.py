import sys
import uinput
import time
import evdev
from dbHandler import Connection
from soundHandler import Sound
from readCardHandler import Reader
from evdev import UInput, ecodes as e

db=Connection('database/testData.db') #CHANGE THIS FOR SEPERATE DATABASE
sound=Sound('./sounds/')
read=Reader('/dev/hidraw0') #CHANGE IF NOT READING INPUT FROM CARD READER
device = evdev.InputDevice('/dev/input/event3') #CHANGE OUTPUTTING ON SPECIFIC INPUT DEVICE

sound.play('accept')
def processCard():
	tag=read.parseCard()
	print('Submitting: ' + tag)
	statusSound=db.removeCredit(tag)
	print(statusSound)
	if statusSound == 'accept':
		print('Accepted credit for: ' + tag)
               	device.write(e.EV_KEY, e.BTN_SELECT, 1)  # CHANGE BUTTON HERE  e.BTN_WHATEVER
		time.sleep(.3)
		device.write(e.EV_KEY, e.BTN_SELECT, 0)  # CHANGE BUTTON HERE TOO
	sound.play(statusSound)

while True:
	processCard()
