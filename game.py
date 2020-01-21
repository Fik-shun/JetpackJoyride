import os
import time
import signal
from alarmexception import AlarmException
from getch import _getChUnix as getChar

from bg import BG
from char import Character
from objects import HorObst,VerObst,Coin,Magnet
from bullet import Bullet

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

beams = [beam,beam2]
coins = [coin,coin2]
bulls = []


# Start Time
gamestart = time.time()
start = gamestart


while player.lives > 0 and player.time > 0:

	player.time = int(TIME + gamestart - time.time())
	# Moving Screen
	now = time.time()
	if now - start > BG_TIME:
		thebg.move_screen(player,bulls)
		start = now

	# Gravity
	if player.position[1] < rows - 1 - player.matrix.shape[0]:
		player.position[1] += 1

	# Magnet 
	if thebg.subx <= magx < thebg.subx + cols:
		if player.position[0] + 2 <= magx:
			player.position[0] += 2		
		else:
			player.position[0] -= 2 

		if player.position[1] + 1 >= magy:
			player.position[1] -= 2		
		else:
			player.position[1] += 2		
			


	objs = [beams,coins,bulls,mag]
	thebg.print(player,objs)

	# takes cursor to beginning
	print("\033[0;0H")
	
	# takes input
	char = user_input()

	if char == 'd':
		player.position[0] += 3
	elif char == 'a':
		player.position[0] -= 3
	elif char == 'w':
		player.position[1] -= 3
	elif char == 's':
		player.position[1] += 3
	elif char == 'f':
		bull = Bullet()
		bull.fire(player)
		bulls.append(bull)

	elif char == 'q' or char == 'Q':
		break	
	
thebg.print_gameEnd()


