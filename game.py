import os
import time
import signal
import math
import random
from alarmexception import AlarmException
from getch import _getChUnix as getChar

from bg import BG
from char import Character
from objects import HorObst,VerObst,DiagObst,Coin,Magnet
from bullet import Bullet, iceBall
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


# getting rows&cols of screen
rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows) - 3
cols = int(cols)

# the background
thebg = BG(rows,cols)


# player
player = Character(5,rows-6)


# Objects

beams = []
coins = []

# Obstacles
for i in range(random.randint(1,7)):
	beams.append(HorObst(random.randint(int(cols/10),int((DRGN_APPRS-0.5)*cols-OBST_LEN)),random.randint(4,rows-5-2)))
for i in range(random.randint(1,7)):
	beams.append(VerObst(random.randint(int(cols/10),int((DRGN_APPRS-0.5)*cols-2)),random.randint(4,rows-5-OBST_LEN)))
for i in range(random.randint(1,3)):
	beams.append(DiagObst(random.randint(int(cols/10),int((DRGN_APPRS-0.5)*cols-OBST_LEN)),random.randint(4,rows-5-OBST_LEN)))

# Coins
for i in range(random.randint(10,25)):
	coins.append(Coin(random.randint(int(cols/10),int((DRGN_APPRS-0.5)*cols)),random.randint(4,rows-5)))


# Magnet
magx = random.randint(int(cols/10),int((DRGN_APPRS-0.5)*cols))
magy = random.randint(4,rows-5)
mag = Magnet(magx,magy)
mag.xrange = int((cols)/4)
mag.yrange = int(2*(rows-4)/3) - 2


# Magnetic border coins
if magy + mag.yrange < rows - 4:
	coins.append(Coin(magx,magy+mag.yrange))
if magy - mag.yrange > 2:
	coins.append(Coin(magx,magy-mag.yrange))
coins.append(Coin(magx+mag.xrange,magy))
coins.append(Coin(magx-mag.xrange,magy))

bulls = []

theboss = Boss(DRGN_APPRS*cols,1)

icebs = []

objs = [beams,coins,bulls,mag,theboss,icebs]


# Start Time
gamestart = time.time()
start = gamestart
uptime = gamestart

while player.lives > 0 and player.time > 0 and theboss.lives > 0:

	# Shield time
	player.time = int(TIME + gamestart - time.time())
	if player.shield == 1 and time.time() - player.shieldStart >= 10:
		player.matrix[0][0] = ' '
		player.shield = 0
		player.shieldEnd = time.time()

	# Moving Screen, and iceBalls firing
	now = time.time()
	if now - start > BG_TIME:
		if thebg.subx < (DRGN_APPRS-0.5)*cols:
			thebg.move_screen(player)
		elif theboss.lives > 0:
			iceb = iceBall()
			if player.position[1]+2 <= theboss.position[1]+theboss.matrix.shape[0]-1:
				iceb.fire([theboss.position[0],player.position[1]+2])
			else:
				iceb.fire([theboss.position[0],theboss.position[1]+theboss.matrix.shape[0]-1])
				
			icebs.append(iceb)
		start = now




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
		uptime = time.time()
				
			
	# Gravity
	elif player.position[1] < rows - 1 - player.matrix.shape[0]:
		player.position[1] += int(4*(time.time()-uptime))


	objs = [beams,coins,bulls,mag,theboss,icebs]
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
		uptime = time.time()
	elif char == 's':
		player.position[1] += player.speed
	elif char == 'f':
		bull = Bullet()
		bull.fire([player.position[0]+5,player.position[1]+2])
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

win = 0
if theboss.lives == 0:
	win = 1
thebg.print_gameEnd(win)



