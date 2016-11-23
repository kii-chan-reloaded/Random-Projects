#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MyMods.py
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

"""
Purely functional modules with no dependencies to other files
"""

def saveArray(full_file_path,array):
	"""
	Saves an array as separate lines in a file
	"""
	with open(full_file_path,"w") as f:
		out=''
		for line in array:
			if isinstance(line,str):
				out += "'"+line+"'\n"
			else:
				out += str(line)+"\n"
		f.write(out)

def loadArray(full_file_path):
	"""
	Opens an array made by the save function
	"""
	with open(full_file_path,"r") as f:
		dirty = f.readlines()
		clean = []
		for line in dirty:
			clean.append(eval(line.replace("\n","")))
		return clean
