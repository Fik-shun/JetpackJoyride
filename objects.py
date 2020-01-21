import numpy as np
from config import *

class Object():

	def __init__(self,x,y):
		
		self.position = [x,y]
		self.display = 1

		# intersect tells if player is intersecting with this obj rn
		# need so as to decrease life only once during 1 intersection

	

class HorObst(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)
		self.matrix = np.full((2, OBST_LEN), "=")

		self.matrix[0][0] = chr(9121)
		self.matrix[0][OBST_LEN-1] = chr(9124)
		self.matrix[1][0] = chr(9123)
		self.matrix[1][OBST_LEN-1] = chr(9126)


class VerObst(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.matrix = np.full((OBST_LEN, 2), '"')	

		self.matrix[0] = [chr(9121),chr(9124)]
		self.matrix[OBST_LEN-1] = [chr(9123),chr(9126)]
		

class Coin(Object):
	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.appearance = '$'

class Magnet(Object):

	def __init__(self,x,y):
		Object.__init__(self,x,y)

		self.matrix = np.full((2, 2), "+")
		self.matrix[0] = [chr(9552),chr(9559)]
		self.matrix[1] = [chr(9552),chr(9565)]
