# NHKEasyNews 2 Printer Bot
Uses my Reddit bot account to recieve messages from my main account, scrape NHK Easy News, download an article, convert it to .pdf, and send it to my printer.

## Use
For myself right now. I'm not willing to try to make this accessable to everyone because there are too many completely random variables involved. If anyone wants one of these for their own, send me an email and we'll talk about what you'll need to do.

Just so I don't forget, here's the options (each need their own line in the message):
+ Url - paste it plain, no extra info needed
+ noPrint - `noPrint=True` or `noPrint=False`. `True` and `False` must be stylized exactly like that (defaults to False)
+ filename - `filename=*.pdf` must end in .pdf (defaults to temp.pdf)
+ rbsize - `rbsize=*` must be number, sets the font size for the furigana (6 is default, gives size 12 text and size 24 title)

As an example, sending the following from my main account:

    http://www3.nhk.or.jp/news/easy/k10010786201000/k10010786201000.html
    rbsize=7
    noPrint=True
    filename=testing.pdf

would save [this](https://drive.google.com/file/d/0BwkDkULgD4CZekZLSnh1UkJpVlk/view?usp=sharing) file to $HOME.

The bot updates once every 10 minutes, or 15 if there's an error.
