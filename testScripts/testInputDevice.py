import sys
from testConfig import settings
fp = open(settings['inputDevice'], 'rb')
print("Test Input Started")
print("Try using the input device")
print("--------------------------")

while True:
    buffer = fp.read(8)
    for c in bytearray(buffer):
        if c > 0:
            print(c)
