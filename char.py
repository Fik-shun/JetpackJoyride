import numpy as np
from colorama import Fore, Back, Style


class Character():

	def __init__(self,x,y):
		
		self.matrix = np.full((5, 4), " ")		
		self.matrix[0] = [' ',' ',' ','W']
		self.matrix[1] = ['#','#','#','O']
		self.matrix[2] = ['#','#','#','X']
		self.matrix[3] = ['#','#','#','X']
		self.matrix[4] = ['"','"','"','X']

		self.position = [x,y]

		self.lives = 5
		self.score = 0

	def get_stats(self):

		thestats = '\tLIVES: ' + str(self.lives) + '\tSCORE: ' + str(self.score) + '\n'
		return thestats

	
