# AutoBonsai

A RPi/Python powered automated Bonsai maintence interface. Inspired by PleaseTakeCareOfMyPlant.com, because I too am going to murder this plant if I have to remember to do everything myself.

Note: I do not own a Bonsai nor any equipment yet. This is just a proof of concept for the moment.

## How it Works - Array-ception
The Schedule is an array maintained by the script. Each term in the array is itself an array with two parts: part one is a time, and the second part is another array of commands as strings. It makes more sense if you look at it:
```
[1479866936.756401, ['waterThePlant()']]
[1479866950.390383, ["lightToggle('off')","notifyMe('Bonsai Update','The light has been turned off')"]]
```
In this example, `waterThePlant` will be executed, then 14 seconds later, `lightToggle` will be executed followed by `notifyMe`.

I'll take pictures of my equipment when I end up getting it.
