import numpy as np
from config import *
from colorama import Fore, Back, Style


class BG():

	def __init__(self,rows,cols):

		# the matrix of game which will be shown
		self.rows = rows
		self.cols = cols
		self.matrix = np.full((rows, WIDTH), " ")
		self.matrix[0] = np.full((1, WIDTH), "|")
		self.matrix[rows-1] = np.full((1, WIDTH), "|")

		self.subx = 0
		self.submatrix = self.matrix[0:rows,0:cols]

	def clear_matrix(self):

		# emptying the matrix
		self.matrix[1:self.rows-1,0:WIDTH] = np.full((self.rows-2, WIDTH), " ")

	def print_matrix(self,toprint):	

		# made string toprint, so that input doesnt interfere on screen
		self.submatrix = self.matrix[0:self.rows,self.subx:self.subx+self.cols]	

		toprint += Back.BLUE + Fore.BLACK		
		for cell in self.submatrix[0][1:]:
			toprint += cell
		toprint += Style.RESET_ALL

		toprint += '\n'
		for row in self.submatrix[1:self.rows-1]:
			for cell in row:
				toprint += cell
			toprint += '\n'
		
		toprint += Back.RED + Fore.BLACK
		for cell in self.submatrix[self.rows-1]:
			toprint += cell
		toprint += Style.RESET_ALL		
		print(toprint)


	def print(self,player,obstacles):

		self.clear_matrix()


		x,y = player.position
		if x <= self.subx:
			player.position[0] = self.subx
		elif x >= self.subx + self.cols - player.matrix.shape[1]:
			player.position[0] = self.subx + self.cols - player.matrix.shape[1]
		if y < 2:
			player.position[1] = 2
				
		x,y = player.position

				
		self.matrix[y:y+player.matrix.shape[0],x:x+player.matrix.shape[1]] = player.matrix

		for obstacle in obstacles:
			x,y = obstacle.position
			self.matrix[y:y+obstacle.matrix.shape[0],x:x+obstacle.matrix.shape[1]] = obstacle.matrix
		
		toprint = player.get_stats()
		
		self.print_matrix(toprint)	
	
	def move_screen(self,player):
		self.subx += 2
		player.position[0] += 2



