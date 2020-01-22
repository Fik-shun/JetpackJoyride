import numpy as np
from config import *

class Shoot():

	def __init__(self):

		self.matrix = np.full((1, 3), "=")
		self.display = 1

	def fire(self,position):

		self.position = position


class Bullet(Shoot):
	
	def __init__(self):
		Shoot.__init__(self)
		self.matrix[0][2] = '>'



class iceBall(Shoot):

	def __init__(self):
		Shoot.__init__(self)
		self.matrix[0][0] = '<'
