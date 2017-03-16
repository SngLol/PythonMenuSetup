#Menu Setup
class menu():
	def __init__(self,name,alt):
		self.name=name
		self.alt=alt
	def inputW(self):
		import msvcrt
		global isInput
		isInput=True
		from msvcrt import getch
		while isInput==True:	#Keypress Input Loop For Windows
			while msvcrt.kbhit()==True:
				msvcrt.getch()
			key = ord(getch())
			# if key == 27: #ESC
				# isInput=False
				# break
			if key == 13: #Enter
				self.next(self.select)
			elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
				key = ord(getch())
				if key == 72: #Up arrow
					if self.select==0:
						self.select=0
					else:
						self.select-=1
				elif key == 80: #Down arrow
					if self.select==len(self.alt)-1:
						self.select=len(self.alt)-1
					else:
						self.select+=1
			if isInput==True:
				self.upt("cls")
	def getkey():	#Keypress Input For Linux Users
		import termios,fcntl,curses,sys,os
		fd = sys.stdin.fileno()
		flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)	# save old state
		attrs_save = termios.tcgetattr(fd)
		attrs = list(attrs_save) # copy the stored version to update
		attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK | termios.ISTRIP | termios.INLCR | termios. IGNCR | termios.ICRNL | termios.IXON )	# iflag
		attrs[1] &= ~termios.OPOST	# oflag
		attrs[2] &= ~(termios.CSIZE | termios. PARENB)	# cflag
		attrs[2] |= termios.CS8
		attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN)	# lflag
		termios.tcsetattr(fd, termios.TCSANOW, attrs)
		fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)	# turn off non-blocking
		try:	# read a single keystroke
			ret = sys.stdin.read(1)	# returns a single character
		except KeyboardInterrupt: 
			ret = 0
		finally:	# restore old state
			termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
			fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
		return ret
	def inputL(self):	#The Startup Menu For Linux Users
		global isInput
		isInput=True
		while isInput==True:	#Keypress Input Loop For Linux
			ret=menu.getkey()
			if ret=="\r":
				self.next(self.select)
			if ret=="A":
				if self.select==0:
					self.select=0
				else:
					self.select-=1
			elif ret=="B":
				if self.select==len(self.alt)-1:
					self.select=len(self.alt)-1
				else:
					self.select+=1
			if isInput==True:
				self.upt("clear")
	def upt(self,clear):
		import os
		self.selectL=[]
		for i in range(0,len(self.alt)):
			self.selectL.append("")
		os.system(clear)
		self.selectL[self.select]="<--"
		print(self.name,"\n")
		for i in range(0,len(self.alt)):
			print(self.alt[str(i)][0],self.selectL[i])
	def next(self,select):
		if self.alt[str(select)][1]==0:
			global isInput
			isInput=False
		else:
			eval(self.alt[str(select)][1]).run()
	def run(self):
		import os,platform
		if platform.system()=="Windows":
			os.system("cls")
		elif platform.system()=="Linux":
			os.system("clear")
		print(self.name,"\n")
		self.selectL=[]
		self.select=0
		for i in range(0,len(self.alt)):
			self.selectL.append("")
			self.selectL[self.select]="<--"
			print(self.alt[str(i)][0],self.selectL[i])
		if platform.system()=="Windows":
			self.inputW()
		elif platform.system()=="Linux":
			self.inputL()

"""
#How to set up your menu:
Name = menu(
	"Title.",				#"Title.\nInformation" if wanted
	{
	"AlternativeNumber0":[	#0-based & in string
		"Alternative",
		"nextMenu"			#Variable name in string / 0 for exit (non-string)
		],
	"AlternativeNumber1":[
		"Alternative",
		"nextMenu"
		]
	}
)

#One line setup:
Name = menu("Title.",{"AlternativeNumber0":["Alternative","nextMenu"],"AlternativeNumber1":["Alternative","nextMenu"]})
"""

#Example Menu list:
a=menu("Hello.",
	{
	"0":[
		"Hi!",
		"b"
		],
	"1":[
		"Bye!",
		"c"
		],
	"2":[
		"Why?",
		"d"
		]
	}
)
b=menu("Bye.",
	{
	"0":[
		"Ok!",
		0
		],
	"1":[
		"Back.",
		"a"
		]
	}
)
c=menu("No.",
	{
	"0":[
		"Ha!",
		0
		],
	"1":[
		"Back.",
		"a"
		]
	}
)
d=menu("I don't know.",
	{
	"0":[
		"Ok!",
		0
		],
	"1":[
		"Back.",
		"a"
		]
	}
)

a.run()
