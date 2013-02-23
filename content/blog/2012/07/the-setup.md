title: The Setup
author: Mike Grouchy
date: 2012-07-18 8:35:00
tags:
    - software
    - programming
    - hardware
    - setup

This post is inspired by [Mahdi](http://www.mahdiyusuf.com/post/16687503726/the-setup) and [The Setup](http://usesthis.com/). I had originally written a rather terrible post about my [development toolbox](http://mikegrouchy.com/blog/my-development-toolbox.html) so I figured it was time to revisit this and get it right for people who care.

##Hardware
Not a lot going on here, nothing fancy. Just macs, running OSX Lion. The hardware is a bit older, but I spend most of my time in a terminal, so I don't really notice so much.

###Work:
* 2008 Aluminum Macbook, 4GB ram
* Magic Mouse
* Standard Apple wired keyboard (I like having the numberpad and not having to be worried about batteries)
* 27" Cinema Display

Out of all these things, I would have to say the cinema display is incredible. I don't normally use my laptop screen when it is connected to the cinema display to avoid [RSI](http://en.wikipedia.org/wiki/Repetitive_strain_injury) issues, however, when I do have it open its normally just for the [rdio](http://rd.io) client.

###Home:
* 2010 iMac 21.5", 8GB Ram
* Magic Mouse
* Apple wireless bluetooth keyboard

I don't use this often, as it is the computer my [wife](http://twitter.com/nicolegrouchy) uses primarily. I only tend to use it when I
don't feel like slogging around with my laptop at home, or I have left it at the [office](http://swixhq.com) or something.


I have also taken to writing drafts for my blogposts using [Github Gists](http://gist.github.com) with my [1st Generation 32GB iPad](http://amzn.to/KLFZrw) and the apple bluetooth keyboard. I have found this to be a fantastic way to write a blogpost or a little code while out at a coffee shop or anywhere else when I am on the go.

##Software
Like I said earlier, I don't spend too much time outside the console, but when I do these are the things I couldn't live without.

* [Moom](http://manytricks.com/moom/) - This is an awesome app, it allows you to tile windows in OSX, attach hotkeys to tiling commands and a bunch of other niceties that don't exist on OSX.
* [rdio](http://rd.io) - As I mentioned earlier, I use rdio. I listen to music all the time while coding, or thinking or just about anything, so I have rdio going basically all the time.
* [Flint](http://giantcomet.com/flint) - We use campfire for team chat in the office so I use flint for that.
* [Chrome](http://chrome.google.com) - The web browser of champions, I pretty much use Chrome exclusively now and normally have way too many tabs open.
* [Skitch](http://skitch.com/) - I use skitch for taking screenshots on OSX it has really great support for simple editing and cropping of your screenshots that I would have a hard time switching to anything else. I dont use their server anymore for storage of my screenshots, I have a proxy set up using [heroku](http://heroku.com) to send my screenshots to a Amazon S3 bucket. This is accomplished with [s3itch](https://github.com/mgrouchy/s3itch).
* [Dropbox](http://db.tt/Hc6Cqm1) -Dropbox is fantastic. I store all the git repos I am working on in Github and it has saved my butt a few times now. I can feel safe everything is backed up and even untracked files(in git) are being versioned, just incase I delete a untracked file I end up needing.
* [Alfred](http://www.alfredapp.com/) - Alfred is an indispensable quick launcher app in the vein of [quicksilver](http://qsapp.com/). I spend most of my time with my hands off the mouse so I don't know what I would do without Alfred.
* [RescueTime](http://rescuetime.com/ref/161860) - I work pretty hard to try to stay productive and at the very least stay knowledgeable about where my time is going. RescueTime helps with that by tracking what I do on the computer every day.

##Command Line Life
The command line is where I spend most of my time, on OSX I don't use the terminal software that comes with OSX, I use [iTerm2](http://www.iterm2.com/). In that terminal I use:

* [Zsh](http://www.zsh.org/) with [Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/), because as you know, [Zsh is your friend](), you can check out my .zshrc in my [dotfiles repo](https://github.com/mgrouchy/dotfiles).
* [Vim](http://www.vim.org/) - The only text editor in my opinion. This is where I spend most of my time check out my [vimfiles](https://github.com/mgrouchy/vim) for setup details.

![vim screenshot](http://img.mikegrouchy.s3.amazonaws.com/1._ControlP_-_%28%7E%29_-_VIM_%28vim%29-20120628-111826.jpg)

* [tmux](http://tmux.sourceforge.net/) - Tmux is great. Its a great alternative to gnu screen, highly configurable and looks great.

![tmux screenshot](http://img.mikegrouchy.s3.amazonaws.com/1._tmux_%28tmux%29-20120628-111332.jpg)

* [bpython](http://bpython-interpreter.org/) - bpython is improved interface to the Python interpreter. It supports syntax highlighting, autocomplete and a bunch of other useful features. I usually have bpython open all day every day.

![bpython screenshot](http://img.mikegrouchy.s3.amazonaws.com/1._bpython_%28Python%29-20120628-111458.jpg)

##On My desk
Books:

* [Natural Language Processing With Python](http://amzn.to/L2qI4V) - Steven Bird, Ewan Klein and Edward Loper
* [Javascript - The Definitive Guide](http://amzn.to/KyjsLo) - David Flanagan
* [Expert Python Programming](http://amzn.to/M3xogV) - Tarek Zaide

A bunch of [Pycoders](http://pycoders.com) stickers

![Pycoders Sickers!](http://mikegrouchy.com/media/images/2012/07/pycoders-stickers.jpg)

Thats about it. What does your setup look like?
