import evdev
from evdev import UInput, ecodes as e

device = evdev.InputDevice('/dev/input/event3')
print(device)



ui = UInput()

# accepts only KEY_* events by default
#device.syn()

#device.close()

for event in device.read_loop():
	print(event.type)
	if event.type == evdev.ecodes.EV_KEY:
		print('something happened')
		print(evdev.categorize(event))
		#device.write(e.EV_KEY, e.BTN_TL, 1)  # KEY_A down
		#device.write(e.EV_KEY, e.BTN_TL, 0)  # KEY_A up

