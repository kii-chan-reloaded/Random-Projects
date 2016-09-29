#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Paste in the path to your steamapps folder
#Default is ~/.steam/steam/steamapps/
STEAMAPPS = '~/.steam/steam/steamapps/'

### Menu building begins
if STEAMAPPS[-1] != '/':
	STEAMAPPS=STEAMAPPS+'/'

from os import popen
from re import search

print("""<openbox_pipe_menu>"
  <item label='Steam'>
    <action name='Execute'>
      <execute>steam</execute>
    </action>
  </item>
  <separator/>""")
GAMES = popen('ls "'+STEAMAPPS+'"*.acf').readlines()
for GAME in GAMES:
	GAME=GAME.replace('\n','')
	ACF=open(GAME,'r').read()
	ID=search('"appid".*"(.*)"',ACF).group(1)
	NAME=search('"name".*"(.*)"',ACF).group(1)
	print '  <item label="'+NAME+'">'
	print '    <action name="Execute">'
	print "      <execute>steam steam://run/"+ID+"</execute>"
	print "    </action>"
	print "  </item>"

print "</openbox_pipe_menu>"
