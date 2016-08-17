#! /usr/bin/python

"""
Assumes a Linux system (Debian, more specifically)
Requires Python libraries re, requests, os, and lxml
Requires program transmission-cli

A simple script that searches Nyaa.se for the newest HorribleSubs torrents. 
Pick the show you wish to download, then pick the quality, and that torrent 
will be added to a fake queue. After all desired torrents are selected, the 
files are downloaded one-by-one, then the script deletes the .torrent files.
All torrents will download to your default Downloads folder as per Transmission.

I love HorribleSubs, and I love Nyaa.se, but even with Adblock their sites 
take *forever* to load on my internet connection. This script was made to 
circumvent the awful wait times and get to downloading faster. Unfortunately,
transmission-cli only allows for one download at a time. I may look into 
other torrent clients to see if their cli allows for multiple downloads, but 
that is fairly low priority, as you'll likely only be downloading a few shows 
per day maximum.
"""

import re
import requests
import os
from lxml import html

def grabShowName(title):
	extName = re.match('(?i)\[horriblesubs\] (.* )+\[.*\].mkv',title.text_content())
	return extName.group(1)

def grabQuality(title,array):
	List=[]
	for listing in array:
		seek = re.match('(?i)\[horriblesubs\] '+title+'\[(.*)\].mkv',listing.text_content())
		if seek:
			List.append(seek.group(1))
	return List

def buildShowName(array):
	List = []
	for listing in array:
		new = grabShowName(listing)
		if new not in List:
			List.append(new)
	return List

def mainFunction(torrs):
	currEps = buildShowName(torrs)
	for i,ep in enumerate(currEps):
		print "("+str(i)+") "+ep
	## Pick a show, any show
	while True:
		selection = raw_input("   Select an episode to download\n    (q to quit): ")
		if selection.isdigit():
			break
		elif selection =="q":
			exit()
		print "Try again"
	SHOW = currEps[int(selection)]
	print "\nSelected "+SHOW+"\n"
	quals = grabQuality(SHOW,torrs)
	for i,qt in enumerate(quals):
		print "("+str(i)+") "+qt
	## Ask for quality
	while True:
		selection = raw_input("   Select a quality to download\n    (q to quit): ")
		if selection.isdigit():
			break
		elif selection =="q":
			exit()
		print "Try again"
	QUAL = quals[int(selection)]
	## Ask if selection is correct, recalls the function if wrong
	while True:
		selection = raw_input("  Download "+SHOW+"at "+QUAL+"?\n    (y to download, n to select again, q to quit): ")
		if selection == "y":
			break
		elif selection == "n":
			return mainFunction(torrs)
		elif selection =="q":
			exit()
		print "Try again"
	## Grab DL link from HTML file
	global allToGet
	for listing in torrs:
		if listing.text_content() == "[HorribleSubs] "+SHOW+"["+QUAL+"].mkv":
			allToGet.append(listing.attrib['href'].replace("//","").replace("view","download"))
	print "\n"+SHOW+"has been added to your download queue.\n"
	## Ask to begin downloads or add another to the queue
	while True:
		selection = raw_input("  Begin downloading?\n    (y to download, n to select another, q to quit): ")
		if selection == "y":
			return allToGet
		elif selection == "n":
			return mainFunction(torrs)
		elif selection =="q":
			exit()
		print "Try again"
	
def startDownloading(dlList):
	for DL in dlList:
		## Downloads the .torrent file
		os.system("wget --output-document='"+os.getcwd()+"/ThisShow.torrent' '"+DL+"'")
		## Starts the download in Transmission
		os.system("transmission-cli --uplimit=0 -D '"+os.getcwd()+"/ThisShow.torrent'")
		## Removes the torrent
		os.system("rm '"+os.getcwd()+"/ThisShow.torrent'")

## Get the search results for HorribleSubs on Nyaa.se
page = requests.get("http://www.nyaa.se/?page=search&cats=1_0&filter=0&term=%5BHorribleSubs%5D")
page = html.fromstring(page.content)
torrs = page.xpath('//td[@class="tlistname"]/a')
## Make one string for the functions to use
allToGet = []
## Do things
getList = mainFunction(torrs)
startDownloading(getList)
## Remove all torrents
os.system('rm ~/.config/transmission/torrents/*')
