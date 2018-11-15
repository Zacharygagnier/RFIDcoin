from dbHandler import Connection
from config import settings

db=Connection(settings['database'])
db.addAllCredit(settings['startupCredits'])
