# Name That Tune!
A simple Python program to manage playing a "Name That Tune"-style game with two teams. Probably best used for larger groups of people, such as a party or convention.

I mostly repurposed the code from my JavaJeopardy Scoreboard for this project.

## Requirements
Linux OS, vlc (cvlc), and Tkinter, built on Python 2.7.11

##How To
Running the script for the first time should create ~/.NTT and ~/.NTT/SongList.txt. Use whatever audio editing software to create the clips you want to play, then export them in ascending numerical order as .mp3s in the ~/.NTT folder (i.e. "1.mp3", "2.mp3", etc). As you do this, add the relevent song information in order to the SongList.txt file (artist, song name, tv show, whatever) with each new line corresponding to the next song (i.e. line 1 is information about 1.mp3, line 2 is information about 2.mp3, etc). Have no more than one blank line feed at the end of the file, otherwise the songs remaining count will be off. If all is done correctly, presssing the "Start song" button will play the song using cvlc, then start the timer. When the clock is reset, the previous song information will appear on the bottom of the window, and the songs remaining will tick down.

##Future work
Might reinstate the "-1" button, but it's not entirely necessary unless you want to be mean about scoring.
