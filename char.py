import numpy as np
from colorama import Fore, Back, Style
from config import *

class Character():

	def __init__(self,x,y):
		
		self.matrix = np.full((5, 4), " ")	

		self.matrix[0] = [' ',' ',' ','0']
		self.matrix[1] = ['/','\\','*',' ']
		self.matrix[2] = ['W','W','|','\\']
		self.matrix[3] = ['Y','Y',':','\\']
		self.matrix[4] = ['"','"','/','/']

		self.position = [x,y]

		self.speed = CHAR_SPEED

		self.lives = LIVES
		self.score = 0
		self.time = TIME

		self.shield = 0
		self.shieldStart = 0
		self.shieldEnd = 0

	def get_stats(self):

		thestats = '\t\tLIVES: ' + str(self.lives) + '\t\tSCORE: ' + str(self.score) + '\t\tTIME REMAINING: ' + str(self.time).zfill(3) + '\n'
		return thestats


	
