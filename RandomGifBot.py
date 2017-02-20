"""

I don't know how much you know already, so I'm assuming you know little
to no Python. This is a multi-line comment, denoted by the three quotation
marks above and below this. Single line and inline comments start with #.

Let's start basic - "print" will send words into the console.

"""

print("Hello! Reddit bot starting up!")

"""

In this next bit here, we're importing praw (Python Reddit API Wrapper).
"Importing" means that you're basically loading another special Python script
called a module. They allow you to do some really fun stuff (line interact
with reddit) without doing a lot of hard work, and they keep your script
looking clean, too.

I have the importing set inside of a try statement, meaning if an error should arise
during this section of code, instead of exiting, it executes the exception
instead. This isn't the best example, because my exception is just to exit,
but it will print a much more human-readable error message than it would
otherwise. We'll see try again later.

"""

try:
    mod = "praw"
    import praw
    mod = "time"
    import time
    mod = "os"
    import os
except:
    exit("Module "+mod+" is required to run this bot. Please install it with pip and run this script again")


# Next up is variables. Normally, I write my bots to prompt the user for
# this information, then save it to a separate file, but for teaching
# purposes we'll put the information right in the file itself.

botRedditUser = "" # Type your bot reddit username in between the quotes. (leave out /u/)
# This is a "string" variable. Basically, it's text.
botRedditPassword = "" # Same deal

botClientID = "" # See below if you don't know what these two are
botSecret = ""

myUsername = ""
mySubreddit = "" # do not put /r/
keyword = "" # You mentioned a keyword in your post for the bot to respond to. Type that here.

sleepTime = 60*5 # This is the number of seconds the bot will wait before
                 # refreshing. Since it's a number, we can do math!
                 # (This will make the bot sleep for 5 minutes)

"""

If you don't know what the client ID or secret are, here's what you do:

1) Go to https://www.reddit.com/prefs/apps and sign in with your bot account.
2) Press the 'create app' button, then enter the following:
     Name: randomGifBot (or whatever you want)
     App type: script
     description: (leave this blank or enter whatever you wish)
     about url: https://github.com/WolfgangAxel/Random-Projects/randomGifBot/RGB.py
     redirect url: http://127.0.0.1:65010/authorize_callback
3) Finally, press the 'create app' button.

"""

reddit = praw.Reddit(client_id = botClientID,
                     client_secret=botSecret,
                     password=botRedditPassword,
                     user_agent="Random GIF bot for /r/"+mySubreddit+", hosted by /u/"+myUsername,
                     username = botRedditUser)
print("Successfully connected to Reddit!")

"""

This is us initializing our connection with Reddit. It's a function provided
by praw. You can look through what they all are over at http://praw.readthedocs.io

Functions are whatever they're named, followed by a list of arguments
in parentheses. They're basically dislocated sections of code that can
be run multiple times with multiple inputs. They're pretty easy to understand.

In fact, why don't we make our own function right now?

"""

def getRandomGif():
    """
    This will be our function to get a new gif from /r/gifs.
    It's a pretty simple function, so we won't take any arguments.
    """
    while True:
        # "while" means that this portion of the code will loop until
        # a condition is met. In this case, our condition is "True".
        # This basically means that this will loop indefinitely or until
        # it is interrupted.
        print("Looking for a gif to send")
        randomPost = reddit.subreddit('gifs').random() # get a random post from gifs
        # Let's check to see if it's a self-post. If we got like a mod announcement
        # or something instead of a gif, this wouldn't be quite as cool.
        if not randomPost.is_self:
            # Another thing- we don't want just any old gif.
            # We want a worthwhile gif.
            # So, we'll set a minimum score for our gifs.
            if randomPost.score >= 250:
                # If it's not a self post, and if the score is good, 
                # then we'll "return" it to the main function.
                # This will probably make more sense later
                print("Found a gif! "+randomPost.url)
                return randomPost.url
"""

And that's it! if the post we get is a self-post, then the "while" loop
makes it start from the top and try again. Here's what it looks like
without my comments:

def getRandomGif():
    while True:
        randomPost = reddit.subreddit('gifs').random()
        if not randomPost.is_self:
            return randomPost.url

With that out of the way, let's write the main loop.

"""

while True: # Our good ol' friend
    try:
        # This will go through and check each comment in the subreddit
        for comment in reddit.subreddit( mySubreddit ).comments():
            print("looking at /u/"+comment.author.name+"'s comment...")
            if keyword not in comment.body:
                print("They don't want a gif.")
                continue
                # "continue" makes python skip the rest of this and start
                # at the top of the "for" loop with the next item
            
            # Now this next part is a little weird.
            # I found out when making this bot that the comment replies
            # function is a little bit buggy. They only show up properly
            # if you pull the comment from the submission as opposed to
            # just looking at the comment straight. So, we have to do a
            # little dance in order to get what we want.
            thisID = comment.id
            submission = comment.submission
            for subComment in submission.comments:
                if subComment.id == thisID:
                    replies = subComment.replies.list()
                    break
            # What that did was go through each comment in the
            # submission that the comment we picked up on was posted in,
            # and when we got to the comment we picked up on earlier, we
            # grabbed all the replies to it and "broke" out of the for loop.
            
            # So what we're going to do with it now is a little advanced
            # bit of scripting. Basically what's going on in this next line
            # is we're going to look through all the replies to the comment
            # and make a list of the (lower case) usernames of the people
            # who replied to it. If the bot had already replied to this
            # comment, it would see it's name in this list and skip it.
            if botRedditUser.lower() in [ reply.author.name.lower() for reply in replies ]:
                print("I already gif'd them.")
                continue
            
            print("They want a gif!")
            randomGifURL = getRandomGif() # We get the URL of a gif
            comment.reply("[Here's your GIFt!]("+randomGifURL+")") # and we reply to the comment
        time.sleep(sleepTime) # sleep (do nothing) until next time
    except Exception as e:
        # This means that if there's any Exceptions (errors) from the code above,
        # we execute this instead, with the error message as the variable e.
        print("There was an error!:\n\n"+str(e.args)) # str() converts a variable into a string.
                                                      # We have to do this since we're adding it
                                                      # to the other string
        time.sleep(60) # Sleep for one minute, then try again.

"""

And there's the bot!!

"""
