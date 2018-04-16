# Rounded Button Twitch Chat

![alt text](https://raw.githubusercontent.com/WolfgangAxel/Random-Projects/master/Streaming/RoundButtonExample.png)

This CSS file overrides the Twitch chat popout window to make the chat slightly more visually appealing. It was created to be used with the OBS
plugin Linux Browser, and presumably will work with the default Browser source for Mac and Windows.

## Instructions For Use

1. Add a (Linux) Browser source to a scene
2. Set the URL to `https://www.twitch.tv/{yourchannel}/chat`
3. Select this CSS file for the custom CSS
4. Adjust page size, zoom, and crop until only the chat area is visible
5. Add a Chroma Key filter
6. Set the Key Color Type to Custom and change the Key Color to `#123123`
7. Adjust the similarity, smoothness, and key color spillreduction to your liking (1, 35, 100 are what I found to work best)
8. Sit back and enjoy!

## Notes

### Dark Theme

Check the comments in the file for recommended hex values for a dark theme!

### Badges

To add badges back into the chat, simply comment out or delete the last section of the file:

    .badges {
        /* Hide badges */
        position:absolute!important;
        visibility:hidden;
    }

### Browser Sizing

What I found works well is 150% zoom and a minimum width of 450px. From here, add a crop filter with 76px top and 168px bottom.
This should perfectly frame your chat without losing any space.
