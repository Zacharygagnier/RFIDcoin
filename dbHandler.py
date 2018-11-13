import sqlite3
from threading import Timer
class Connection:
	def __init__(self, dbName):
		self.conn = sqlite3.connect(dbName)
		self.conn.row_factory = sqlite3.Row
		self.c = self.conn.cursor()
		self.insertNext = False

	def  insertNew(self, ID):
		self.c.execute('INSERT OR IGNORE INTO user(tag, type, credit, name, creation_date) VALUES(' + ID + ', 1, 10, "undefined", datetime("now"))')
		self.conn.commit()
		return 'created'

	def insertTimeOut(self):
		self.insertNext = False

	def removeCredit(self, ID):
		if self.insertNext:
			return self.insertNew(ID)
		self.c.execute('SELECT * FROM user WHERE tag=' + str(ID))
		user=self.c.fetchone()
		if user == None:
			return 'reject'
		type=user[2]
		credits=user[3]
		if type == -1:
			self.insertNext = True
			return 'create'
		if user is None or credits == 0 and type > 0:
			return 'reject'

		self.c.execute('UPDATE user SET credit=' + str(credits-1) + ' WHERE tag=' + str(ID))
		self.conn.commit()
		return "accept"

	def addAllCredit(self):
		self.c.execute('update user SET credit=10 where credit<10')
		self.conn.commit()
