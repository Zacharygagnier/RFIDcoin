import evdev
from evdev import ecodes as e
from testConfig import settings
device = evdev.InputDevice(settings['outputDevice'])
print(device)

print("Test Input Started")
print("Try using the output device")
print("--------------------------")

for event in device.read_loop():
    print(event.type)
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))