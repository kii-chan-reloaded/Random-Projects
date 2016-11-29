#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nhkpdf.py
#  
#  2016 Keaton Brown <linux.keaton@gmail.com>
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

from bs4 import BeautifulSoup as BS
from os import system as run
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from math import ceil,floor
from requests import get
import praw
import OAuth2Util
from time import sleep
from re import search

def _force_unicode(text):
	if text == None:
		return u''
	if isinstance(text, unicode):
		return text
	try:
		text = unicode(text, 'utf-8')
	except UnicodeDecodeError:
		text = unicode(text, 'latin1')
	except TypeError:
		text = unicode(text)
	return text

def force_utf8(text):
	return str(_force_unicode(text).encode('utf8'))

def ripRubies(htmlSection):
	sect = soup.find(id=htmlSection)
	rubies=[]
	text=[]
	isRuby = False
	isReading = False
	for part in sect.descendants:
		if part.name == 'ruby':
			isRuby = True
		elif part.name == 'rt':
			isReading = True
		elif not part.name:
			if (not isReading and not isRuby):
				if part == "":
					text.append("\n")
				else:
					text.append(force_utf8(part))
				rubies.append(None)
			if isReading:
				rubies.append(force_utf8(part))
				isReading = False
			if isRuby:
				text.append(force_utf8(part))
				isRuby = False
	return text,rubies

def addSpaces(text,rubies):
	textstring = ""
	rubystring = ""
	for i,part in enumerate(rubies):
		if not part:
			textstring += text[i]
			if text[i] == "\n":
				rubystring += " \n"
			else:
				for x in range(len(text[i])/3):
					rubystring += "　　"
			continue
		partL = len(part)/3
		textL = len(text[i])/3
		textstring += text[i]
		rubystring += part
		if partL > textL*2:
			for x in range(int(ceil((partL-(textL*2))/2.0))):
				textstring += "　"
				textL +=1
		if partL < textL*2:
			for x in range(int((textL*2)-partL)):
				rubystring += "　"
	return textstring,rubystring

def manualBreak(S,wide):
	breakPoint=wide*3
	brokenS = []
	for line in S.splitlines():
		while breakPoint<len(line):
			brokenS.append(line[:breakPoint])
			line = line[breakPoint:]
		if not line.strip("　") == "":
			brokenS.append(line)
	return brokenS

def makePDF(filename,titleText,titleRubies,text,rubies,rbsize):
	txsize=rbsize*2
	titrbsize = rbsize*2
	tittxsize = txsize*2
	c=canvas.Canvas("/home/keaton/"+filename)
	pdfmetrics.registerFont(TTFont('Jap1','/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'))
	blankLineRemover = 0
	for i in range(len(titleText)):
		if titleText[i]=="":
			blankLineRemover += 1
			continue
		c.setFont('Jap1', titrbsize)
		marginW = 0.5*inch
		marginH = 10.5*inch
		c.drawString(marginW,marginH-(titrbsize+tittxsize+5)*(i-blankLineRemover),titleRubies[i+1])
		c.setFont('Jap1', tittxsize)
		c.drawString(marginW,marginH-(titrbsize+tittxsize+5)*(i-blankLineRemover)-tittxsize,titleText[i])
	offset = len(titleText)-blankLineRemover
	blankLineRemover = 0
	for i in range(len(text)):
		if text[i]=="":
			blankLineRemover += 1
			continue
		c.setFont('Jap1', rbsize)
		c.drawString(marginW,marginH-(offset*(tittxsize+titrbsize+20))-(rbsize+txsize+10)*(i-blankLineRemover),rubies[i+1])
		c.setFont('Jap1', txsize)
		c.drawString(marginW,marginH-(offset*(tittxsize+titrbsize+20))-(rbsize+txsize+10)*(i-blankLineRemover)-txsize,text[i])
	c.showPage()
	c.save()

def scrapeAndPrint(url,noPrint,filename,rbsize):
	global soup
	soup = BS(get(url).content,'html.parser')

	articleText,articleRubies = ripRubies("newsarticle")
	titleText,titleRubies = ripRubies("newstitle")

	articleText,articleRubies = addSpaces(articleText,articleRubies)
	titleText,titleRubies = addSpaces(titleText,titleRubies)
	
	wide = int(inch*7.5/(rbsize*2)-1)/2*2

	articleText = manualBreak(articleText,wide)
	articleRubies = manualBreak(articleRubies,wide*2)
	titleText = manualBreak(titleText,wide/2)
	titleRubies = manualBreak(titleRubies,wide)
	makePDF(filename,titleText,titleRubies,articleText,articleRubies,rbsize)
	if not noPrint:
		quietly = run("lpr -r "+filename)

def getPMs():
	for mail in reddit.get_unread(unset_has_mail=True, update_user=True, limit=None):
		Body = force_utf8(mail.body)
		if str(force_utf8(mail.author)).lower() != "omnipotence_is_bliss":
			reddit.send_message("Omnipotence_is_bliss","Somebody who is not me sent me a message. Weird.")
			continue
		articleLink = search('(?i)http(.*)html',Body)
		if articleLink:
			articleLink = articleLink.group()
			noPrint = search('(?i)noPrint=(True|False)',Body)
			if not noPrint:
				noPrint = False
			else:
				noPrint = noPrint.group(1)
			filename = search('(?i)filename=(.*pdf)',Body)
			if not filename:
				filename = "temp.pdf"
			else:
				filename = filename.group(1)
			rbsize = search('(?i)rbsize=(.*)',Body)
			if not rbsize:
				rbsize = 6
			else:
				rbsize = int(rbsize.group(1))
			scrapeAndPrint(articleLink,noPrint,filename,rbsize)
		mail.mark_as_read()
		mail.reply("Operation performed successfully")

reddit = praw.Reddit(user_agent= "RoboRuri, automatically printing NHK articles - hosted by /u/Omnipotence_is_bliss")
auth = OAuth2Util.OAuth2Util(reddit, print_log = True, configfile = "/home/keaton/Documents/RoboRuri2/MyFiles/oauth.ini")
auth.refresh(force=True)

if __name__ == '__main__':
	print "Beginning inbox monitoring..."
	while True:
		getPMs()
		try:
			getPMs()
			sleep(600)
		except Exception as e:
			print "Looks like I'm having issues (internet?). I will try again in 15 minutes.\n\nError details: "+str(e.args)
			sleep(900)
