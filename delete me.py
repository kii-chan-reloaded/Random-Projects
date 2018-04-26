# I'm at work but I needed to write this down.

from requests import post, get
from Secret import username, password
from re import search

########
# Runs in bkg to interface with gnudip
# Set up cron job for like once every hour. Less than that if I can find a service that returns my public IP through API
######
# Edit: It should be possible to poll my router for my public IP. Do testing when you get home

#currIP = post("https://gnudip.datasystems24.net/gnudip/cgi-bin/gnudip.cgi",form={"username":username,"password":password,"domain":"freedombox.rocks","page":"login","localaddr":"nojava","login":"Login"}).text
currIP = ""

curr = search(r"(?:i)Currently Points to ([\d\.]+)",currIP).group(1)
me = search(r"(?:i)GnuDIP has IP address ([\d\.]+)",currIP).group(1)

if curr != me:
    fixIP = post("https://gnudip.datasystems24.net/gnudip/cgi-bin/gnudip.cgi",form={"username":username,"password":password,"domain":"freedombox.rocks","page":"login","localaddr":"nojava","updatehost":"Go","updateaddr":IP})
