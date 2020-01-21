import numpy as np
from config import *

class Bullet():

	def __init__(self):

		self.matrix = np.full((1, 3), "=")
		self.matrix[0][2] = '>'
		self.display = 1

	def fire(self,player):

		self.position = [player.position[0]+5,player.position[1]+2]

