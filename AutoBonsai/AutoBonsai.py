#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AutoBonsai.py
#  
#  Copyright 2016 keaton <keaton@MissionControl>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

## Variables
sleepTime = 30*60				# Check the schedule twice an hour
wateringSleep = 6*60*60			# Check the water levels 4 times a day
lightOnTime = 10*60*60			# Turn the light on for 10 hours a day


## Definitions
def addEvent(date,commands):
	"""
	adds an event to the schedule
	'date' should be a time in seconds since epoch
	'commands' will be passed through exec when 'date' is past (can be string or array of strings)
	"""
	global Schedule
	if type(commands) is not list:
		commands=[commands]
	Schedule.append([date,commands])
	# sort the array by epoch time
	Schedule=sorted(Schedule,key=lambda i: i[0])
	saveArray(MYDIR+"/MyFiles/Schedule.list",Schedule)

def checkEvent():
	"""
	Checks to see if an event needs to be triggered
	"""
	global Schedule
	if Schedule != []:
		if time() >= Schedule[0][0]:
			for command in Schedule[0][1]:
				exec(command)
			Schedule=Schedule[1:]
			saveArray(MYDIR+"/MyFiles/Schedule.list",Schedule)
			checkEvent()

def notifyMe(title,message):
	post('https://api.simplepush.io/send',data={'key':'36h2Me', 'title':str(title), 'msg':str(message)})

## Modules
from time import time,sleep
from os import path
from requests import post
from sys import path as moduleDir

MYDIR = path.dirname(path.realpath(__file__))
moduleDir.append(MYDIR+"/Modules")

from MyMods import *
from PlantUtils import *

Schedule = []
try:
	Schedule = loadArray(MYDIR+"/MyFiles/Schedule.list")
except:
	print "Schedule not found."

if __name__ == '__main__':
	print "hi!"
	if Schedule == []:
		print "Schedule not found or empty. Initiating and scheduling all care commands"
		beginCaring()		
	while True:
		sleep(sleepTime)
		checkEvent()
