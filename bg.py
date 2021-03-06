import numpy as np
from config import *
from colorama import Fore, Back, Style


class BG():

	def __init__(self,rows,cols):

		# the matrix of game which will be shown
		self.__rows = rows
		self.__cols = cols
		self.__matrix = np.full((rows, WIDTH), " ")
		self.__matrix[0] = np.full((1, WIDTH), "|")
		self.__matrix[rows-1] = np.full((1, WIDTH), "|")

		self.__bg_move = 1

		self.__subx = 0
		self.__submatrix = self.__matrix[0:rows,0:cols]



	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a	

	@property
	def rows(self):
		return self.__rows
	@rows.setter
	def rows(self, a):
		self.__rows = a

	@property
	def cols(self):
		return self.__cols
	@cols.setter
	def cols(self, a):
		self.__cols = a

	@property
	def bg_move(self):
		return self.__bg_move
	@bg_move.setter
	def bg_move(self, a):
		self.__bg_move = a

	@property
	def subx(self):
		return self.__subx
	@subx.setter
	def subx(self, a):
		self.__subx = a

	@property
	def submatrix(self):
		return self.__submatrix
	@submatrix.setter
	def submatrix(self, a):
		self.__submatrix = a

	
	



	def clear_matrix(self):

		# emptying the matrix
		self.matrix[1:self.rows-1,0:WIDTH] = np.full((self.rows-2, WIDTH), " ")

	def print_matrix(self,player):	

		# made string toprint, so that input doesnt interfere on screen
		self.submatrix = self.matrix[0:self.rows,self.subx:self.subx+self.cols]	

		toprint = player.get_stats()
		toprint += Back.BLUE + Fore.BLACK		
		for cell in self.submatrix[0][1:]:
			toprint += cell
		toprint += Style.RESET_ALL

		toprint += '\n'
		toprint += Fore.YELLOW
		for row in self.submatrix[1:self.rows-1]:
			for cell in row:
				toprint += cell
			toprint += '\n'
		toprint += Style.RESET_ALL
		
		toprint += Back.RED + Fore.BLACK
		for cell in self.submatrix[self.rows-1]:
			toprint += cell
		toprint += Style.RESET_ALL		
		print(toprint)


	def print(self,player,objs):

		self.clear_matrix()

		# player display
		x,y = player.position	
		if x <= self.subx:
			player.position[0] = self.subx
		elif x >= self.subx + self.cols - player.matrix.shape[1]:
			player.position[0] = self.subx + self.cols - player.matrix.shape[1]
		if y < 2:
			player.position[1] = 2				
		elif y > self.rows - 6:
			player.position[1] = self.rows - 6				

		x,y = player.position

		self.matrix[y:y+player.matrix.shape[0],x:x+player.matrix.shape[1]] = player.matrix

		# as objs = [beams,coins]
		# obstacle display and collision	
		for obstacle in objs[0]:
			if obstacle.display == 1:
				x,y = obstacle.position
				h,w = obstacle.matrix.shape
				x2,y2 = player.position
				h2,w2 = player.matrix.shape
				# check collision, if yes deleting obstacle
				self.matrix[y:y+h,x:x+w] = obstacle.matrix
				if (y<=y2<y+h or y2<=y<y2+h2) and (x<=x2<x+w or x2<=x<x2+w2):
					obstacle.display = 0
					if player.shield == 0:
						player.lives -= 1

			

		# coin display and collision	
		for coin in objs[1]:	
			if coin.display == 1:
				x,y = coin.position
				h,w = [1,1]
				x2,y2 = player.position
				h2,w2 = player.matrix.shape
				# check collision
				self.matrix[y:y+1,x:x+1] = coin.appearance

				if (y<=y2<y+h or y2<=y<y2+h2) and (x<=x2<x+w or x2<=x<x2+w2):
					player.score += 1
					coin.display = 0


		# bullet display and collision	
		for bull in objs[2]:
			x2,y2 = bull.position
			h2,w2 = bull.matrix.shape
			if bull.display == 1:
				bull.position[0] += BULL_SPEED
				self.matrix[y2:y2+h2,x2:x2+w2] = bull.matrix
				for obstacle in objs[0]:
					if obstacle.display == 1:
						x,y = obstacle.position
						h,w = obstacle.matrix.shape
						# check collision
						if (y<=y2<y+h or y2<=y<y2+h2) and (x<=x2<x+w or x2<=x<x2+w2):
							player.score += 1
							obstacle.display = 0
							bull.display = 0
				if self.subx >= (DRGN_APPRS-0.5)*self.cols:
						x,y = objs[4].position
						h,w = objs[4].matrix.shape
						# check collision
						if (y<=y2<y+h or y2<=y<y2+h2) and (x<=x2<x+w or x2<=x<x2+w2):
							player.score += 1
							objs[4].lives -= 1
							obstacle.display = 0
							bull.display = 0	
		# magnet				
		x,y = objs[3].position
		h,w = objs[3].matrix.shape
		self.matrix[y:y+h,x:x+w] = objs[3].matrix
		
		# Dragon				
		if objs[4].lives > 0:
			x,y = objs[4].position
			h,w = objs[4].matrix.shape
			self.matrix[y:y+h,x:x+w] = objs[4].matrix

			# Dragon Movement
			if self.subx >= (DRGN_APPRS-0.5)*self.cols:
				if y + 13 < player.position[1]:
					if objs[4].position[1] < self.rows - 2 - objs[4].matrix.shape[0]:
						objs[4].position[1] += DRGN_SPEED

				elif objs[4].position[1] > DRGN_SPEED:
					objs[4].position[1] -= DRGN_SPEED


		# iceBalls display and collision	
		for iceb in objs[5]:
			x2,y2 = iceb.position
			h2,w2 = iceb.matrix.shape
			if iceb.display == 1:
				iceb.position[0] -= ICEB_SPEED
				self.matrix[y2:y2+h2,x2:x2+w2] = iceb.matrix
				x,y = player.position
				h,w = player.matrix.shape
				# check collision
				if (y<=y2<y+h or y2<=y<y2+h2) and (x<=x2<x+w or x2<=x<x2+w2):
					if player.shield == 0:
						player.lives -= 1
					iceb.display = 0		




				

		self.print_matrix(player)	
	

	def move_screen(self,player):
		self.subx += self.bg_move
		player.position[0] += self.bg_move


	def print_gameEnd(self,win):
		self.submatrix = np.full((self.rows, self.cols), " ")

		toprint = Back.BLUE + Fore.BLACK		
		for cell in self.submatrix[0][1:]:
			toprint += cell
		toprint += Style.RESET_ALL
		if win == 1:
			a = Fore.GREEN+"""                                                                                                                               
      ***** *    **         * ***         ***** *    **           ***** *    **   ***          * ***         ***** *     **    
   ******  *  *****       *  ****      ******  *  *****        ******  *  *****    ***       *  ****      ******  **    **** * 
  **   *  *     *****    *  *  ***    **   *  *     *****     **   *  *     *****   ***     *  *  ***    **   *  * **    ****  
 *    *  **     * **    *  **   ***  *    *  **     * **     *    *  **     * **      **   *  **   ***  *    *  *  **    * *   
     *  ***     *      *  ***    ***     *  ***     *            *  ***     *         **  *  ***    ***     *  *    **   *     
    **   **     *     **   **     **    **   **     *           **   **     *         ** **   **     **    ** **    **   *     
    **   **     *     **   **     **    **   **     *           **   **     *         ** **   **     **    ** **     **  *     
    **   **     *     **   **     **    **   **     *           **   **     *         ** **   **     **    ** **     **  *     
    **   **     *     **   **     **    **   **     *           **   **     *         ** **   **     **    ** **      ** *     
    **   **     *     **   **     **    **   **     *           **   **     *         ** **   **     **    ** **      ** *     
     **  **     *      **  **     **     **  **     *            **  **     *         **  **  **     **    *  **       ***     
      ** *      *       ** *      *       ** *      *             ** *      *         *    ** *      *        *        ***     
       ***      *        ***     *         ***      *              ***      ***      *      ***     *     ****          **     
        *********         *******           ********                ******** ********        *******     *  *****              
          **** ***          ***               ****                    ****     ****            ***      *     **               
                ***                                                                                     *                      
    ********     ***                                                                                     **                    
  *************  **                                                                                                            
 *           ****                                                                                                              
                                                                                                                               """
		else:

			a = Fore.RED + """                                                                                                                                   
      ***** *    **         * ***         ***** *    **           ***** *             * ***          *******      ****           * 
   ******  *  *****       *  ****      ******  *  *****        ******  *            *  ****        *       ***   *  *************  
  **   *  *     *****    *  *  ***    **   *  *     *****     **   *  *            *  *  ***      *         **  *     *********    
 *    *  **     * **    *  **   ***  *    *  **     * **     *    *  *            *  **   ***     **        *   *     *  *         
     *  ***     *      *  ***    ***     *  ***     *            *  *            *  ***    ***     ***           **  *  **         
    **   **     *     **   **     **    **   **     *           ** **           **   **     **    ** ***            *  ***         
    **   **     *     **   **     **    **   **     *           ** **           **   **     **     *** ***         **   **         
    **   **     *     **   **     **    **   **     *           ** **           **   **     **       *** ***       **   **         
    **   **     *     **   **     **    **   **     *           ** **           **   **     **         *** ***     **   **         
    **   **     *     **   **     **    **   **     *           ** **           **   **     **           ** ***    **   **         
     **  **     *      **  **     **     **  **     *           *  **            **  **     **            ** **     **  **         
      ** *      *       ** *      *       ** *      *              *              ** *      *              * *       ** *      *   
       ***      *        ***     *         ***      *          ****           *    ***     *     ***        *         ***     *    
        *********         *******           ********          *  *************      *******     *  *********           *******     
          **** ***          ***               ****           *     *********          ***      *     *****               ***       
                ***                                          *                                 *                                   
    ********     ***                                          **                                **                                 
  *************  **                                                                                                                
 *           ****                                                                                                                  
                                                                                                                                   """
		lines = a.split('\n')
		for i in range(21):
			self.submatrix[i] = [c for c in lines[i]] + [' ']*(self.cols-len(lines[i]))
		for i in range(self.rows):
			for j in range(self.cols):
				toprint += self.submatrix[i][j]
			toprint += '\n'
		
		toprint += Back.RED + Fore.BLACK
		for cell in self.submatrix[self.rows-1]:
			toprint += cell
		toprint += Style.RESET_ALL		
		print('                                                                                         ')	
		print(toprint)