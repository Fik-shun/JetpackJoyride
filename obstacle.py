import numpy as np
class Obstacle():

	def __init__(self,x,y):
		

		self.position = [x,y]

	

class HorObst(Obstacle):

	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)
		self.matrix = np.full((2, 11), " ")		
		self.matrix[0] = [chr(9121),'=','=','=','=','=','=','=','=','=',chr(9124)]
		self.matrix[1] = [chr(9123),'=','=','=','=','=','=','=','=','=',chr(9126)]


class VerObst(Obstacle):

	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)
		self.matrix = np.full((11, 2), " ")		
		self.matrix[0] = [chr(9121),chr(9124)]
		for i in range(1,10):
			self.matrix[i] = ['"','"']
		self.matrix[10] = [chr(9123),chr(9126)]
		