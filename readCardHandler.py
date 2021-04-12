import sys
import time
from threading import Timer


class Reader:
    def __init__(self, bufferInput='/dev/hidra41w0'):
        self.fp = open(bufferInput, 'rb')

    def parseCard(self):
        string = {'string': ''}

        def cancelString(totalString):
            totalString['string'] = ''
        timeout = Timer(2.5, cancelString, [string])
        while True:
            buffer = self.fp.read(8)
            for c in bytearray(buffer):
                if c > 29 and c < 41:
                    if not timeout.isAlive():
                        timeout = Timer(2.5, cancelString, [string])
                        timeout.start()
                    if c == 40:
                        if timeout.isAlive():
                            timeout.cancel()
                        return string['string']
                    else:
                        if c == 39:
                            string['string'] = string['string'] + '0'
                        else:
                            string['string'] = string['string'] + \
                                chr(c+19)
