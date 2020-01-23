import numpy as np
from config import *

class Shoot():

	def __init__(self):

		self.__matrix = np.full((1, 3), "=")
		self.__display = 1

	def fire(self,position):
		self.__position = position
	
	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a

	@property
	def display(self):
		return self.__display
	@display.setter
	def display(self, a):
		self.__display = a	



	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, a):
		self.__position = a	



class Bullet(Shoot):
	
	def __init__(self):
		Shoot.__init__(self)
		self.matrix[0][2] = '>'
	def fire(self,position):
		self.position = position
		a = 1


class iceBall(Shoot):

	def __init__(self):
		Shoot.__init__(self)
		self.matrix[0][0] = '<'
