import numpy as np
from config import *

class Object():

	def __init__(self,x,y):
		
		self.__position = [x,y]

		self.__display = 1

		# intersect tells if player is intersecting with this obj rn
		# need so as to decrease life only once during 1 intersection

	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, a):
		self.__position = a
	
	@property
	def display(self):
		return self.__display
	@display.setter
	def display(self, a):
		self.__display = a	


class HorObst(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)
		self.__matrix = np.full((2, OBST_LEN), "=")

		self.__matrix[0][0] = chr(9121)
		self.__matrix[0][OBST_LEN-1] = chr(9124)
		self.__matrix[1][0] = chr(9123)
		self.__matrix[1][OBST_LEN-1] = chr(9126)

	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a

class VerObst(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.__matrix = np.full((OBST_LEN, 2), '"')	

		self.__matrix[0] = [chr(9121),chr(9124)]
		self.__matrix[OBST_LEN-1] = [chr(9123),chr(9126)]
	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a

class DiagObst(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)
		self.__matrix = np.full((OBST_LEN,OBST_LEN), ' ')

		np.fill_diagonal(self.__matrix, '\\')
	
	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a

class Coin(Object):
	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.__appearance = '$'
	@property
	def appearance(self):
		return self.__appearance
	@appearance.setter
	def appearance(self, a):
		self.__appearance = a

class Magnet(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.__xrange = 0
		self.__yrange = 0

		self.__matrix = np.full((2, 2), "+")
		self.__matrix[0] = [chr(9552),chr(9559)]
		self.__matrix[1] = [chr(9552),chr(9565)]
	
	@property
	def xrange(self):
		return self.__xrange
	@xrange.setter
	def xrange(self, a):
		self.__xrange = a

	@property
	def yrange(self):
		return self.__yrange
	@yrange.setter
	def yrange(self, a):
		self.__yrange = a	

	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a