import numpy as np
from config import *

class Boss():
	
	def __init__(self,x,y):
		
		self.__position = [x,y]
		self.__display = 1
		self.__matrix = np.full((31, 65), " ")
		self.__lives = DRGN_LIVES


		a = """                                         _\\/
                                     _.-'.'`)
               .                  .-'     `-.         __\\/
                \\.    .  |,   _.-'     -:`````)   _.-'.'``)
                 \\`.  |\\ | \\.-_.         `._ _.-'  .'`
                __) )__\\ |! )/ \\_.        _.-'    `.
            _.-'__`-' =`:' /.' / |     .-'    -:`````)
      __.--' ( (@> ))  = \\ ^ `'. |_..-'         `.
     : @       `^^^    == \\ ^   `. |<             `.
     VvvvvvvvVvvvv)    =  ;   ^  ;_/ :        -:`````)
       (^^^^^^^^^^=  ==   |      ; \\. :         `.
    ((  `----------.  == |  ^   ^;_/   :          `.
   __/\\__         /==   /        : \\.  :   _..--`````)
>><_  __```---.._/ ====/  ^    ^  :/  :      `.    
    \\/   `._    /===  /     ^    `  .    _.--```)
     __/\\__    ;===  /        ^   .'      `.
  >><__  __``--...__-.' ^     /          .--``)        ---     
       \\/   :=`--...__.--''     ^   ._.-'  |         .'...`.  (
      ((      .| ===   \\      ^          `.|_.      ; :  `.'   )
          .-'   \\====   \\  ^ .  ^    ^     `.|_.    ; '.   `../_
        ..'      :===    \\.-'            ^  `. |    ;  `;       \\
      .-'  ^      \\ ^  .-'    ^    ^  ;      ; /    ;   ;       )
     .'^     ^   :=`-'           ^  _'       ; \\.  ; ^  ;      (
    :    ^    .--'    ^      ^__.--"   ^     ;_/  ;     ;
     `.^   ^:          ^_.-"\\    ^           ; \\ ; ^   ;
       `-._.: ^   ^_.-"\\ === \\      ^       \\;_/'     ;
            _`-._     `.\\===  \\  ^                 .;'
    __..--''    _`-.._`. `.== `\\        ^    ^   ;'
   (-(-(-(-(--'' fksh.''.`.`\\= `\\.  ^      ^   .'
             __..---''  .'`-`)`-..`-..____...-'
            (-(-(-(-(-''     '                                   """

		lines = a.split('\n')
		for i in range(31):
			self.__matrix[i] = [c for c in lines[i]] + [' ']*(65-len(lines[i]))

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

	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self, a):
		self.__matrix = a

	@property
	def lives(self):
		return self.__lives
	@lives.setter
	def lives(self, a):
		self.__lives = a    
      
