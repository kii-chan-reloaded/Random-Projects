#!/bin/bash
GAMEDIR="$HOME/Games/GameBoy"
GAMES="$(ls $GAMEDIR | grep -E '*.gb|*.gba')"
readarray -t ENTRY < <(echo "$GAMES")

PS3="Choose a game to load: "
select option in "${ENTRY[@]}" Cancel
do
    case $option in
        "${ENTRY[$REPLY-1]}")
			      pulseaudio -k;
            vbam --opengl-nearest --flash-size=1 --bios=$GAMEDIR/gba_bios.bin --rtc "$GAMEDIR/${ENTRY[$REPLY-1]}";
            pulseaudio --start;
            break;;
        Cancel)
            break;;
     esac
done

exit
