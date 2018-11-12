import os

class Sound:
	def __init__(self, directory):
		self.path=directory
		self.sounds={'accept': "coinPositive.mp3",
			 'reject': "coinNegative.mp3",
			 'create': "creationStart.mp3",
			 'created': "cardCreated.mp3"}
	def play(self, soundNum):
		os.system('mpg123 -q ' + self.path + self.sounds[soundNum] + '&')

