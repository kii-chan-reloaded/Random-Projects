#SteamPipe
SteamPipe is a pipemenu for the Openbox WM. It will populate a menu with all Steam games installed in a list of steamapps folders. Clicking on a game will launch it.

##Usage
If you have a steamapps folder outside of the default install directory, open the script and update the STEAMAPPS variable to include the additional directories.

To add the pipe to your Openbox menu, add `<menu execute="python /PATH/TO/THIS/FILE/steampipe.py" id="steampipe" label="Steam"/>` to your menu.xml file, replacing `/PATH/TO/THIS/FILE/` with wherever you save this script to (i.e. if you save this to a folder called "Scripts" in your Documents folder, replace it with `~/Documents/Scripts/`). Reconfigure Openbox and it should work.

Alternatively, if you use ObMenu, go to Add->Pipemenu, change the Label to `Steam`, the Id to `steampipe`, and the Execute to `python /PATH/TO/THIS/FILE/steampipe.py`, once again following the outline above for replacing `/PATH/TO/THIS/FILE/`
