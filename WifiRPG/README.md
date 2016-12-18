# Wi-Fi Random Passphrase Generator

Mostly inspired by the [XKCD comic](https://xkcd.com/936/). This script uses a bank of adverbs, adjectives, and nouns to generate a somewhat-sensible passphrase for your router. 

## Usage

Arguments:

+ `-h/--help` ==> Prints the help dialog and quits
+ `-a/--add TYPE WORD` ==> Adds a word to a list. `TYPE` is one of `adv`, `adj`, or `noun`. Words with spaces must be in quotes.
+ `--test` ==> MUST BE LAST. Use instead of `--reset` to run the generation but not execute `RouterPasswording.py`. Good for testing your reset commands.
+ `--reset` ==> MUST BE LAST. Uses the rest of the line as the custom command to update your display. See `-h` for more info.

Requires all 5 files in the same directory.

## Work on your part

1. You will have to do some reverse engineering on your router to figure out how to update the password yourself. As of right now, I have not worked extensively on that yet, but I will detail instructions on how to do that when I get it figured out.

2. You will need to create your own system of displaying the passphrase somewhere. I would recommend one or more of: some form of display management on a screen, email notifications, having the passphrase automatically printed on physical paper, a morse code LED, a button that uses speech synthesis to say the passphrase when pressed, etc etc.

3. Last but certainly not least, it is EXTREMELY HIGHLY RECOMMENDED you either append 2-3 times as many new words to each wordbank, or generate a completely new wordbank of 100+ words a piece yourself (100^3 = 1,000,000 unique passphrases). Random passphrase generation is relatively meaningless if someone has your wordbanks. Grab your favorite dictionary or go to one of the many random word generators out there and go to town on it. 
