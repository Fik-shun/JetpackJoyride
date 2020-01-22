import os
import time
import signal
import math
from alarmexception import AlarmException
from getch import _getChUnix as getChar

from bg import BG
from char import Character
from objects import HorObst,VerObst,Coin,Magnet
from bullet import Bullet
from boss import Boss

from config import *


def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.1):
	''' input method '''
	signal.signal(signal.SIGALRM, alarmhandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	
	try:
		text = getChar()()
		signal.alarm(0)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''


#getting rows&cols of screen
rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows) - 3
cols = int(cols)

#the background
thebg = BG(rows,cols)


#player
player = Character(5,rows-6)


# Objects
beam = HorObst(int(cols/3),int((rows-4)/2))
beam2 = VerObst(3*int(cols/4),int((rows-4)/4))

coin = Coin(6*int(cols/7),int((rows-4)/7))
coin2 = Coin(6*int(cols/11),int((rows-4)/7))


magx = 14*int(cols/11)
magy = int((rows-4)/7)
mag = Magnet(magx,magy)
mag.xrange = int((cols)/4)
mag.yrange = int(2*(rows-4)/3) - 2

coin3 = Coin(magx,magy+mag.yrange)
coin4 = Coin(magx+mag.xrange,magy)
coin6 = Coin(magx-mag.xrange,magy)

theboss = Boss(2*cols,1)


beams = [beam,beam2]
coins = [coin,coin2,coin3,coin4,coin6]
bulls = []


# Start Time
gamestart = time.time()
start = gamestart


while player.lives > 0 and player.time > 0:

	player.time = int(TIME + gamestart - time.time())
	if player.shield == 1 and time.time() - player.shieldStart >= 10:
		player.matrix[0][0] = ' '
		player.shield = 0
		player.shieldEnd = time.time()

	# Moving Screen
	now = time.time()
	if now - start > BG_TIME and thebg.subx < 1.5*cols:
		thebg.move_screen(player)
		start = now

	# Gravity
	if player.position[1] < rows - 1 - player.matrix.shape[0]:
		player.position[1] += 1

	# Magnet 
	if math.pow(abs(magx - player.position[0]),2)/math.pow(mag.xrange,2) + math.pow(abs(magy - player.position[1]),2)/math.pow(mag.yrange,2) <=  1:  
		if player.position[0] + 2 <= magx:
			player.position[0] += 2		
		else:
			player.position[0] -= 2 

		if player.position[1] + 1 >= magy:
			player.position[1] -= 2		
		else:
			player.position[1] += 2		
			


	objs = [beams,coins,bulls,mag,theboss]
	thebg.print(player,objs)

	# takes cursor to beginning
	print("\033[0;0H")
	
	# takes input
	char = user_input()

	if char == 'd':
		player.position[0] += player.speed
	elif char == 'a':
		player.position[0] -= player.speed
	elif char == 'w':
		player.position[1] -= player.speed
	elif char == 's':
		player.position[1] += player.speed
	elif char == 'f':
		bull = Bullet()
		bull.fire(player)
		bulls.append(bull)
	elif char == ' ' and player.shield == 0 and time.time() - player.shieldEnd >= 60:
		player.shield = 1
		player.matrix[0][0] = 'S'
		player.shieldStart = time.time()
	elif char == 'c' and thebg.bg_move == 1:
		thebg.bg_move = 2
		player.speed = 6

	elif char == 'q' or char == 'Q':	
		break	
	
thebg.print_gameEnd()


