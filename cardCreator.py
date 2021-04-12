import sys
import time
from config import settings
from dbHandler import Connection
from readCardHandler import Reader
from threading import Timer

db = Connection(settings['database'])
reader = Reader(settings['inputDevice'])


def createCard():
    string = {'string': ''}
    name = input("What name should this card have?: ")
    type = input(
        "What privelage does this card have? -1 = debug 0=admin 1=user: ")
    credit = input("How many credits should this card start with?: ")
    print("Scan card now")
    db.insertNew(reader.parseCard(), type, credit, name)
    answer = input("Card Created, create another? y/n: ")


while True:
    if createCard() == 'n':
        sys.exit()
