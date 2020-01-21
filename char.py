import numpy as np
from colorama import Fore, Back, Style
from config import *

class Character():

	def __init__(self,x,y):
		
		self.matrix = np.full((5, 4), " ")		
		self.matrix[0] = [' ',' ',' ','W']
		self.matrix[1] = ['#','#','#','O']
		self.matrix[2] = ['#','#','#','X']
		self.matrix[3] = ['#','#','#','X']
		self.matrix[4] = ['"','"','"','X']

		self.position = [x,y]

		self.lives = LIVES
		self.score = 0
		self.time = TIME

	def get_stats(self):

		thestats = '\t\tLIVES: ' + str(self.lives) + '\t\tSCORE: ' + str(self.score) + '\t\tTIME REMAINING: ' + str(self.time).zfill(3) + '\n'
		return thestats

			
	
