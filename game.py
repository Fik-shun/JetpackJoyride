import os
import time
import signal
from alarmexception import AlarmException
from getch import _getChUnix as getChar

from bg import BG
from char import Character
from obstacle import HorObst,VerObst

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
beam = HorObst(int(cols/3),int((rows-4)/2))
beam2 = VerObst(3*int(cols/4),int((rows-4)/4))

beams = [beam,beam2]

start = time.time()


while player.lives > 0:

	# Moving Screen
	now = time.time()
	if now - start > 0.3:
		thebg.move_screen(player)
		start = now

	# Gravity
	if player.position[1] < rows - 1 - player.matrix.shape[0]:
		player.position[1] += 1

	thebg.print(player,beams)
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
	elif char == 'q':
		exit()	




