import numpy as np
from colorama import Fore, Back, Style
from config import *

class Character():

	def __init__(self,x,y):
		
		self.__matrix = np.full((5, 4), " ")	

		self.__matrix[0] = [' ',' ',' ','0']
		self.__matrix[1] = ['/','\\','*',' ']
		self.__matrix[2] = ['W','W','|','\\']
		self.__matrix[3] = ['Y','Y',':','\\']
		self.__matrix[4] = ['"','"','/','/']

		self.__position = [x,y]

		self.__speed = CHAR_SPEED

		self.__lives = LIVES
		self.__score = 0
		self.__time = TIME

		self.__shield = 0
		self.__shieldStart = 0
		self.__shieldEnd = 0



	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a
	
	@property
	def lives(self):
		return self.__lives
	@lives.setter
	def lives(self, a):
		self.__lives = a	

	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, a):
		self.__position = a

	@property
	def speed(self):
		return self.__speed
	@speed.setter
	def speed(self, a):
		self.__speed = a

	@property
	def shield(self):
		return self.__shield
	@shield.setter
	def shield(self, a):
		self.__shield = a

	@property
	def shieldStart(self):
		return self.__shieldStart
	@shieldStart.setter
	def shieldStart(self, a):
		self.__shieldStart = a

	@property
	def shieldEnd(self):
		return self.__shieldEnd
	@shieldEnd.setter
	def shieldEnd(self, a):
		self.__shieldEnd = a

	@property
	def score(self):
		return self.__score
	@score.setter
	def score(self, a):
		self.__score = a

	@property
	def time(self):
		return self.__time
	@time.setter
	def time(self, a):
		self.__time = a	


	def get_stats(self):

		thestats = '\t\tLIVES: ' + str(self.__lives) + '\t\tSCORE: ' + str(self.__score) + '\t\tTIME REMAINING: ' + str(self.__time).zfill(3) + '\n'
		return thestats


	
