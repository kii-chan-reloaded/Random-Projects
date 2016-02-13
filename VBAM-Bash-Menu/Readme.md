#VBA-M Bash Menu
A simple script to automagically detect GBA ROMs and launch them using VBA-M. Rather niche as it is now, but could be applied to many other programs

Created because Pulseaudio was causing VBA-M to randomly crash for seemingly no consistent reason on my machine, but Pulseaudio is needed for too many other applications to get rid of it completely. This allows me to temporarily disable Pulseaudio while I play games with VBA-M and restart it when I'm done.

##Practical uses
- Forces the use of ALSA over Pulseaudio for the duration of a command, then restarts it.
- Adds a fake GUI for launching games with VBA-M
- Could be modified to list all images of one type in a folder and convert only the ones you select to a new format
- Other oddball cases like that one

##Things to change for your own use
- Directory for games/files to load (change grep accordingly if not for GBA ROMs)
- Menu commands (Remove Pulseaudio killing, remove break, or change command - whatever is necessary)
- Variable names, if you so wish
