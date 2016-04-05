#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import time
import os
import random

class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.HOME = os.path.expanduser("~")
		os.system("cd $HOME/.NTT || mkdir $HOME/.NTT")
		self.songListFile = "%s/.NTT/SongList.txt" % self.HOME
		
		try:
			self.songString = open(self.songListFile).read()
		except:
			os.system("> $HOME/.NTT/SongList.txt")
			self.songString = open(self.songListFile).read()
		
		
		self.songArray = self.songString.splitlines()
		self.songNumber = len(self.songArray)
		
		self.grid()
		
		self.timeOut = Tkinter.StringVar()
		self.timeOut.set("Time's up!")
		self.noMore = Tkinter.StringVar()
		self.noMore.set("No more songs!")
		
		self.timeValue = Tkinter.IntVar()
		self.timeValue.set(30)
		
		self.songRemaining = Tkinter.IntVar()
		self.songRemaining.set(self.songNumber)
		
		self.songRandom = random.sample(range(self.songNumber), self.songNumber)
		os.system("> $HOME/.NTT/RandomList.txt")
		self.newSongList = range(self.songNumber)
		for item in range(self.songNumber):
			self.newSongList[item] = self.songArray[self.songRandom[item]]
		self.randomList = open('/home/keaton/.NTT/RandomList.txt','rw+')
		self.randomList.writelines( "%s\n" % item for item in self.newSongList )
		self.randomList.close()
		
		self.countUp = Tkinter.IntVar()
		self.countUp.set(0)
		
		self.songsLeft = Tkinter.StringVar()
		self.labelSongsLeft = Tkinter.Label(self,textvariable=self.songsLeft,font=("DwarfFortressVan", 50))
		self.labelSongsLeft.grid(column=0,row=0,columnspan=3,sticky="NSEW")
		self.plzwork = "Songs left: %r" % self.songRemaining.get()
		self.songsLeft.set(self.plzwork)
		if self.songRemaining.get() == 0:
			self.labelSongsLeft.config(textvariable=self.noMore)
		
		self.button_R = Tkinter.Button(self,text=u"+1",fg="white",bg="red",command=self.addred,font=("DwarfFortressVan", 50))
		self.button_R.grid(column=0,row=1,sticky='NSWE')
		
		self.button_B = Tkinter.Button(self,text=u"+1",fg="white",bg="blue",command=self.addblue,font=("DwarfFortressVan", 50))
		self.button_B.grid(column=2,row=1,sticky='NSWE')
		
		self.button_ST = Tkinter.Button(self, text=u"Start Clock",command=self.startClock, relief="raised",font=("DwarfFortressVan", 50))
		self.button_ST.grid(column=1,row=1,sticky='NSWE')
		
		self.redScore = Tkinter.IntVar()
		self.labelRed = Tkinter.Label(self,textvariable=self.redScore,fg="white",bg="red",font=("DwarfFortressVan", 50))
		self.labelRed.grid(column=0,row=2,sticky='NSEW')
		self.redScore.set(0)
		
		self.blueScore = Tkinter.IntVar()
		self.labelBlue = Tkinter.Label(self,textvariable=self.blueScore,fg="white",bg="blue",font=("DwarfFortressVan", 50))
		self.labelBlue.grid(column=2,row=2,sticky='NSEW')
		self.blueScore.set(0)
		
		self.timeCountdown = Tkinter.IntVar()
		self.labelTime = Tkinter.Label(self,textvariable=self.timeCountdown,font=("DwarfFortressVan", 50))
		self.labelTime.grid(column=1,row=2,sticky='NSEW')
		self.timeCountdown.set(self.timeValue.get())
		
		self.lastPlayed = Tkinter.StringVar()
		self.labelLP = Tkinter.Label(self,textvariable=self.lastPlayed,font=("DwarfFortressVan", 50))
		self.labelLP.grid(column=0,row=3,columnspan=3,sticky="NSEW")
		self.lastPlayed.set("Name That Tune!")
		
		
		
		self.timerStart = Tkinter.BooleanVar()
		self.timerStart.set(False)
		
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=3)
		self.grid_columnconfigure(2,weight=1)
		self.grid_rowconfigure(0,weight=2)
		self.grid_rowconfigure(1,weight=1)
		self.grid_rowconfigure(2,weight=1)
		self.grid_rowconfigure(3,weight=2)
		self.resizable(True,True)
		self.update()
		self.geometry(self.geometry())
		
	def addred(self):
		self.redScore.set(self.redScore.get()+1)
		
	def addblue(self):
		self.blueScore.set(self.blueScore.get()+1)

	def startClock(self):
		if self.button_ST.config('relief')[-1] == "sunken":
			self.button_ST.config(relief="raised")
			self.button_ST.config(text="Start Clock")
			self.timerStart.set(False)
			self.timeCountdown.set(self.timeValue.get())
			self.labelTime.config(textvariable=self.timeCountdown)
			if self.songRemaining.get() == 0:
				self.labelSongsLeft.config(textvariable=self.noMore)
			self.lastPlayed.set(self.newSongList[self.countUp.get()-1])
			self.plzwork = "Songs left: %r" % self.songRemaining.get()
			self.songsLeft.set(self.plzwork)
		else:
			self.button_ST.config(relief="sunken")
			self.button_ST.config(text="Reset Clock")
			self.timeCountdown.set(self.timeValue.get())
			self.playsnip()
			self.timerStart.set(True)
			self.countdown()
	
	def playsnip(self):
		self.countUp.set(self.countUp.get()+1)
		self.play = "cvlc --play-and-exit %s/.NTT/%r.mp3" % (self.HOME, self.songRandom[self.countUp.get()-1]+1)
		os.system(self.play)
		self.songRemaining.set(self.songRemaining.get()-1)	
		
	
	def countdown(self):
		if self.timerStart.get():
			if self.timeCountdown.get()>0:
				self.timeCountdown.set(self.timeCountdown.get()-1)
				self.after(1000,self.countdown)
			else:
				self.labelTime.config(textvariable=self.timeOut)
				self.timerStart.set(False)
		
if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('Name That Tune!')
	app.mainloop()
