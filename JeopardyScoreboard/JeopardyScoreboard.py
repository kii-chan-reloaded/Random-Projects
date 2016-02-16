#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import time

class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		
		self.timeOut = Tkinter.StringVar()
		self.timeOut.set("Time's up!")
		
		self.timeValue = Tkinter.IntVar()
		self.entry = Tkinter.Entry(self,textvariable=self.timeValue)
		self.entry.grid(column=4,row=0,sticky='EW')
		self.timeValue.set(20)
		
		self.RWag = Tkinter.IntVar()
		self.entry = Tkinter.Entry(self,textvariable=self.RWag)
		self.entry.grid(column=3,row=1,sticky='EW')
		
		self.BWag = Tkinter.IntVar()
		self.entry = Tkinter.Entry(self,textvariable=self.BWag)
		self.entry.grid(column=5,row=1,sticky='EW')
		
		self.button_R50 = Tkinter.Button(self,text=u"+50",fg="white",bg="red",command=self.add50red)
		self.button_R50.grid(column=0,row=0,sticky='WE')
		
		self.button_R100 = Tkinter.Button(self,text=u"+100",fg="white",bg="red",command=self.add100red)
		self.button_R100.grid(column=1,row=0,sticky='WE')
		
		self.button_R500 = Tkinter.Button(self,text=u"+500",fg="white",bg="red",command=self.add500red)
		self.button_R500.grid(column=2,row=0,sticky='WE')
		
		self.button_B50 = Tkinter.Button(self,text=u"+50",fg="white",bg="blue",command=self.add50blue)
		self.button_B50.grid(column=6,row=0,sticky='WE')
		
		self.button_B100 = Tkinter.Button(self,text=u"+100",fg="white",bg="blue",command=self.add100blue)
		self.button_B100.grid(column=7,row=0,sticky='WE')
		
		self.button_B500 = Tkinter.Button(self,text=u"+500",fg="white",bg="blue",command=self.add500blue)
		self.button_B500.grid(column=8,row=0,sticky='WE')
		
		self.button_R50S = Tkinter.Button(self,text=u"-50",fg="white",bg="red",command=self.sub50red)
		self.button_R50S.grid(column=0,row=1,sticky='WE')
		
		self.button_R100S = Tkinter.Button(self,text=u"-100",fg="white",bg="red",command=self.sub100red)
		self.button_R100S.grid(column=1,row=1,sticky='WE')
		
		self.button_R500S = Tkinter.Button(self,text=u"-500",fg="white",bg="red",command=self.sub500red)
		self.button_R500S.grid(column=2,row=1,sticky='WE')
		
		self.button_B50S = Tkinter.Button(self,text=u"-50",fg="white",bg="blue",command=self.sub50blue)
		self.button_B50S.grid(column=6,row=1,sticky='WE')
		
		self.button_B100S = Tkinter.Button(self,text=u"-100",fg="white",bg="blue",command=self.sub100blue)
		self.button_B100S.grid(column=7,row=1,sticky='WE')
		
		self.button_B500S = Tkinter.Button(self,text=u"-500",fg="white",bg="blue",command=self.sub500blue)
		self.button_B500S.grid(column=8,row=1,sticky='WE')
		
		self.button_ST = Tkinter.Button(self, text=u"Start Clock",command=self.startClock, relief="raised")
		self.button_ST.grid(column=4,row=1,sticky='WE')
		
		self.button_RWagP = Tkinter.Button(self,text=u"Add",fg="white",bg="red",command=self.RAddWager)
		self.button_RWagP.grid(column=3,row=0,sticky='WENS')
		
		self.button_RWagM = Tkinter.Button(self,text=u"Sub",fg="white",bg="red",command=self.RSubWager)
		self.button_RWagM.grid(column=3,row=2,sticky='WENS')
		
		self.button_BWagP = Tkinter.Button(self,text=u"Add",fg="white",bg="blue",command=self.BAddWager)
		self.button_BWagP.grid(column=5,row=0,sticky='WENS')
		
		self.button_BWagM = Tkinter.Button(self,text=u"Sub",fg="white",bg="blue",command=self.BSubWager)
		self.button_BWagM.grid(column=5,row=2,sticky='WENS')
		
		self.redScore = Tkinter.IntVar()
		self.labelRed = Tkinter.Label(self,textvariable=self.redScore,fg="white",bg="red",font=("DwarfFortressVan", 25))
		self.labelRed.grid(column=0,row=2,columnspan=3,sticky='EW')
		self.redScore.set(0)
		
		self.blueScore = Tkinter.IntVar()
		self.labelBlue = Tkinter.Label(self,textvariable=self.blueScore,fg="white",bg="blue",font=("DwarfFortressVan", 25))
		self.labelBlue.grid(column=6,row=2,columnspan=3,sticky='EW')
		self.blueScore.set(0)
		
		self.timeCountdown = Tkinter.IntVar()
		self.labelTime = Tkinter.Label(self,textvariable=self.timeCountdown,font=("DwarfFortressVan", 25))
		self.labelTime.grid(column=4,row=2,sticky='EW')
		self.timeCountdown.set(self.timeValue.get())
		
		self.timerStart = Tkinter.BooleanVar()
		self.timerStart.set(False)
		
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)
		self.grid_columnconfigure(3,weight=1)
		self.grid_columnconfigure(4,weight=1)
		self.grid_columnconfigure(5,weight=1)
		self.grid_columnconfigure(6,weight=1)
		self.grid_columnconfigure(7,weight=1)
		self.grid_columnconfigure(8,weight=1)
		self.resizable(True,False)
		self.update()
		self.geometry(self.geometry())
		
	def add50red(self):
		self.redScore.set(self.redScore.get()+50)
		
	def add100red(self):
		self.redScore.set(self.redScore.get()+100)
		
	def add500red(self):
		self.redScore.set(self.redScore.get()+500)
		
	def add50blue(self):
		self.blueScore.set(self.blueScore.get()+50)
		
	def add100blue(self):
		self.blueScore.set(self.blueScore.get()+100)
		
	def add500blue(self):
		self.blueScore.set(self.blueScore.get()+500)
		
	def sub50red(self):
		self.redScore.set(self.redScore.get()-50)
		
	def sub100red(self):
		self.redScore.set(self.redScore.get()-100)
		
	def sub500red(self):
		self.redScore.set(self.redScore.get()-500)
		
	def sub50blue(self):
		self.blueScore.set(self.blueScore.get()-50)
		
	def sub100blue(self):
		self.blueScore.set(self.blueScore.get()-100)
		
	def sub500blue(self):
		self.blueScore.set(self.blueScore.get()-500)
		
	def RAddWager(self):
		self.redScore.set(self.redScore.get()+self.RWag.get())
		
	def RSubWager(self):
		self.redScore.set(self.redScore.get()-self.RWag.get())
		
	def BAddWager(self):
		self.blueScore.set(self.blueScore.get()+self.BWag.get())
		
	def BSubWager(self):
		self.blueScore.set(self.blueScore.get()-self.BWag.get())
		
	def startClock(self):
		if self.button_ST.config('relief')[-1] == "sunken":
			self.button_ST.config(relief="raised")
			self.button_ST.config(text="Start Clock")
			self.timerStart.set(False)
			self.timeCountdown.set(self.timeValue.get())
			self.labelTime.config(textvariable=self.timeCountdown)
		else:
			self.button_ST.config(relief="sunken")
			self.button_ST.config(text="Reset Clock")
			self.timeCountdown.set(self.timeValue.get())
			self.timerStart.set(True)
			self.countdown()
	
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
	app.title('Jeopardy Scoreboard')
	app.mainloop()
