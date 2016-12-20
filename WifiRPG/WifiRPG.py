#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  WifiRPG.py
#  Wi-Fi Random Passphrase Generator
#  
#  Copyright 2016 Keaton Brown <linux.keaton@gmail.com>
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

import sys

helpDialog = """
      WifiRPG - Wi-Fi Random Passcode Generator
   Intended for use on a Raspberry Pi hooked up to
   a monitor/display system in your home. Use it to
   generate secure, random passphrases for your home
   Wi-Fi network, then display the password on the
   screen. For automatic passphrase updating, set
   the following as a monthly cron job:
   python3 {path}/WifiRPG.py --reset {your passphrase display commands}

Usage:
  .../WifiRPG.py [-a/--add TYPE WORD] [--reset/--test]

Arguments:
  -a, --add ............. Adds a word to a list. 
             :. noun   :  These words will be saved to the
             :. adj    :  appropriate file and henceforth used as
             :. adv    :. potential passphrase material
  -h, --help ............ Prints this dialog and exits
  --test ................ Follows the same rules as --reset, doesn't actually
                       :. change the router password
  --reset ............... Uses the rest of the line as a custom 
                       :  command to update your display. Note: the
                       :  new password will be added as the final
                       :  argument in the command or it will be
                       :  substituted where "{PASSPHRASE}" is typed
                       :  For example -
                       :    myScript.sh --new-password {PASSPHRASE} --more
                       :  would be executed like so -
                       :    myScript.sh --new-password xxxxxxxxxx --more
                       :  Furthermore -
                       :    myScript.sh
                       :  would be executed as -
                       :.   myScript.sh xxxxxxxxxx
""".replace("{path}",sys.path[0])

def entropy(password):
	L = len(password)
	from math import log
	#########################################################################
	# From https://en.wikipedia.org/wiki/Password_strength#Random_passwords #
	H = log((26+10) + (26*2+10+1)**4 + (26*2+1)**(L-6) + 26,2)
	#       0-9,A-Z   0-9,A-Z,a-z,-    A-Z,a-z,-        a-z                 #
	# The first character is known to be in either 0-9 or A-Z               #
	# Characters 2-5 could pull from 0-9, A-Z, a-z, or -                    #
	# The last character is known to be in a-z                              #
	# The remaining middle characters could be from A-Z, a-z, or -          #
	#########################################################################
	return H


def maybeNumber():
	from random import random
	TorF = random()
	if TorF < 0.5:
		return True
	elif TorF > 0.5:
		return False
	else:
		return maybeNumber()
	

def resetPass(customCommand,test=False):
	from random import sample as randomize
	from random import random
	from os.path import exists
	# Opens the Adj, Adv, and Noun files as arrays
	av = open(sys.path[0]+"/Adv").read().splitlines()
	aj = open(sys.path[0]+"/Adj").read().splitlines()
	nn = open(sys.path[0]+"/Noun").read().splitlines()
	# Just for fun, some statistics!
	totalCombos = len(av)*len(aj)*len(nn)
	combosFormatted = "{:,}".format(totalCombos)
	avLengths=[]
	for item in av:
		avLengths.append(len(item))
	ajLengths=[]
	for item in aj:
		ajLengths.append(len(item))
	nnLengths=[]
	for item in nn:
		nnLengths.append(len(item))
	from statistics import mean,median,mode
	print("-"*25+"\n"+
		  "Total adverbs: "+str(len(av))+"\n"+
		  "Total adjectives: "+str(len(aj))+"\n"+
		  "Total nouns: "+str(len(nn))+"\n"+
		  "Total possible combinations: "+combosFormatted+" (not factoring in numbers)\n"+
		  "Shortest possible passphrase length: "+str(min(avLengths)+min(ajLengths)+min(nnLengths))+"\n"+
		  "Longest possible passphrase length: "+str(max(avLengths)+max(ajLengths)+max(nnLengths)+5)+"\n"+
		  "Mean passphrase length: "+str(int(mean(avLengths)+mean(ajLengths)+mean(nnLengths)+4))+"\n"+
		  "Median passphrase length: "+str(int(median(avLengths)+median(ajLengths)+median(nnLengths))+4)+"\n"+
		  "Mode passphrase length: "+str(int(mode(avLengths)+mode(ajLengths)+mode(nnLengths))+4)+"\n"+
		  "-"*25)
	# Randomize the order of the arrays
	av = randomize(av,len(av))
	aj = randomize(aj,len(aj))
	nn = randomize(nn,len(nn))
	# Pick a random word from each randomized array
	newAdverb = av[int(random()*len(av))].capitalize()
	newAdjective = aj[int(random()*len(aj))].capitalize()
	newNoun = nn[int(random()*len(nn))].capitalize()
	# Possibly add a random number from 1 to 10,000
	if maybeNumber():
		from math import ceil
		number = str(ceil(random()*10000))
	else:
		number = ''
	# Assemble the passphrase
	newPassphrase = number+newAdverb+newAdjective+newNoun
	#################################################################### Needs attention
	print("The new passphrase will be: "+newPassphrase)
	print("Total entropy: ~"+str(int(entropy(newPassphrase))))
	if customCommand == ' {PASSPHRASE}':
		print("Password display command not found. Aborting.")
		exit()
	if not test:
		import RouterPasswording
		RouterPasswording.newPassphrase(newPassphrase)
	from os import system as execute
	execute(customCommand.replace("{password}",newPassphrase).replace("{passphrase}",newPassphrase))


def makeAddition(newWord,fileExt):
	with open(fileExt,"r") as wordbank:
		wordbank = wordbank.read()
		parsable = wordbank.splitlines()
	newWord = ''.join([word.capitalize()+'-' for word in newWord.split()],)[:-1]
	if newWord.lower() in [word.lower() for word in parsable]:
		print("The word '"+newWord+"' was already in the list of words.")
		return
	with open(fileExt,"a") as output:
		if wordbank[-1] == "\n":
			output.write(newWord+"\n")
		else:
			output.write("\n"+newWord+"\n")
	print("The word '"+newWord+"' was successfully added to the list of words.")

def checkAdditions():
	if "-a" in args:
		if args[args.index("-a")+1] == 'noun':
			makeAddition(args[args.index("-a")+2],sys.path[0]+"/Noun")
		if args[args.index("-a")+1] == 'adj':
			makeAddition(args[args.index("-a")+2],sys.path[0]+"/Adj")
		if args[args.index("-a")+1] == 'adv':
			makeAddition(args[args.index("-a")+2],sys.path[0]+"/Adv")
		args.remove('-a')
		checkAdditions()

if __name__ == '__main__':
	args = [arg for arg in sys.argv[1:]]
	if (args == []) or (("-h" or "--help") in args):
		print(helpDialog)
		exit()
	checkAdditions()
	if "--test" in args:
		customCommand = ''
		for commandBit in args[args.index("--test")+1:]:
			customCommand=customCommand+commandBit+" "
		if "{passphrase}" not in customCommand.lower():
			customCommand = customCommand+" {PASSPHRASE}"
		resetPass(customCommand,test=True)
	if "--reset" in args:
		customCommand = ''
		for commandBit in args[args.index("--reset")+1:]:
			customCommand=customCommand+commandBit+" "
		if "{passphrase}" not in customCommand.lower():
			customCommand = customCommand+" {PASSPHRASE}"
		resetPass(customCommand)
