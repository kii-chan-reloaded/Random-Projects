#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PlantUtils.py
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

from __main__ import *
#from gpiozero import ????????

def lightToggle(state):
	if state == 'on':
		print "light on"
		addEvent(time()+lightOnTime,"lightToggle('off')")
	elif state == 'off':
		print 'light off'
		addEvent(time()+(24*60*60-lightOnTime),"lightToggle('on')")
	notifyMe("Bonsai Update","The light has been turned "+state)

def checkWater():
	return True

def waterThePlant():
	if checkWater():
		print "Watering..."
		notifyMe("Bonsai Update","The tree has been given water")
		addEvent(time()+wateringSleep,"waterThePlant()")

def beginCaring():
	lightToggle('on')
	waterThePlant()
