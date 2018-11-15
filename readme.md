This repository is a script to read inputs from an rfid reader or a similar reader that outputs numbers and ends with the enter key.
This script works by first reading inputs from /dev/hidraw, checks the database listed, and sends an event to a
controller you have currently plugged in to emulate a keypress using /dev/input/event

Currently that's the only way I have of both reading input from only a specific device as a background script and sending
a key event to retroarch. If you have a better way that can actually work with retroarch, please let me know since it seems to
an active issue in retroarch.

the button press to change is located in rfid.py as well as the database location, input device, and output device
the keys that can be used are located here https://www.freedesktop.org/software/libevdev/doc/1.4/kernel_header.html HOWEVER I've noticed you have to use a key that is availible on the controller itself


dependencies and installs

sudo apt-get update
sudo apt-get install libudev-dev
git clone https://github.com/tuomasjjrasanen/python-uinput.git
cd python-uinput
python setup.py build
sudo python setup.py install
cd ..
sudo apt-get install alsa-utils mpg123
sudo apt-get install sqlite3
sudo apt-get install python-pip
sudo pip install evdev

there are multiple files:
rfid.py is the main script which can be started in the background by launcher.sh
cardCreator.py is a small command line program to add new cards with specific accesses and credits if you want to add more information than using the debug card with rfid.py
testOutputDevice.py is a small script to run seperately to determine the /dev/input/event device and determine which button is availible to use
addCreditSchedule.py is a script that can be scheduled to run once every so often, this will reset credits to their maximum once depleted whenever it is run


the database used is sqlite and can be created with:
CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, tag TEXT UNIQUE, type INTEGER, credit INTEGER, name TEXT, creation_date DATETIME, last_played DATETIME);
