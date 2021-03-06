title: Compile Vim with Python support on OSX with Homebrew
author: Mike Grouchy
Date: 2012-05-09 10:17:00
tags:
    - python
    - vim
    - homebrew
    - OSX

[Mahdi](http://twitter.com/myusuf3) asked me today how I compiled Vim with +Python
on OSX and I couldn't remember the exact commands, so I am writing this blog post
so I will remember in the future and because someone else might find this useful.

Compiling Vim with +Python or +Ruby is required if you want to run any plugins
that have peices that are written in those languages. The usual way around this
on OSX is to just install [MacVim](https://github.com/b4winckler/macvim) and use
that. However, if you really want to use terminal Vim, you are out of luck on OSX.

So this is where [Homebrew](http://mxcl.github.com/homebrew/) comes in, we can use Homebrew to compile vim from a custom
formula. The only requirements to do this are [Mercurial](http://mercurial.selenic.com/) and Homebrew.

You can install Mercurial by using either easy_install or pip:

```bash
#install mercurial
sudo easy_install mercurial
#or
sudo pip install mercurial
```
You can follow the directions on the [Homebrew Github Wiki](https://github.com/mxcl/homebrew/wiki/installation) to install homebrew.

Now you can Install this Homebrew formula which has been modified slightly to my tastes
to install Vim.

<script src="https://gist.github.com/2051422.js?file=vim.rb"></script>

To install this formula you can just use this command, or fork the Gist and modify
the formula as you see fit(that's what I did) to install your flavor of Vim.

```bash
brew install https://raw.github.com/gist/2051422/0cfce544a4ab86318221c4d7213306a7b7ec7b3d/vim.rb
```

By default the Vim compiled with this script is compiled with +python and +ruby,
if you want support for other interpreters you can pass those parameters to the script with:

```bash
--enable-interp=NAME,...", "lua, mzscheme, perl, python, python3, tcl and/or ruby"
```

You can also specify vim be compiled with features(the scripts, default is normal)
To see what the features do, you can see this [rather ugly table](http://www.drchip.org/astronaut/vim/vimfeat.html)

```bash
--with-features=TYPE", "tiny, small, normal, big or huge"
```

Now that you have vim installed with your interpreters and features compiled,
go ahead and check the version:

```bash
vim --version
```

and you should see that it is the updated version.

If you don't see that it is the updated version, it means your /usr/local/bin isn't
on your path, or if it is on your path it comes after usr/bin.

So how do you fix this?

##Option 1: Update your path:
In your .zshrc ([you are using Zsh right?](http://mikegrouchy.com/blog/zsh-is-your-friend.html)) or .bashrc
update your path.

```bash
#this
export PATH=/usr/bin:/usr/sbin
#to this
export PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin
```

##Option 2: Move your old Vim and symlink the new one
You can move the Vim that comes with OSX and Symlink the one brew installed

```bash
sudo mv /usr/bin/vim /usr/bin/oldvim
ln -s /usr/local/bin/vim /usr/bin/vim
```

One of those should solve your problem.

##Protip:
You may notice that your terminal Vim does not support backspace in Insert mode
with the settings I have setup in the brew formula.

If this is something you want, you can stick this line in your .vimrc:

```viml
set backspace=indent,eol,start
```

I think that should be it. If you have any questions leave it in the comments or
ask me on [twitter](http://twitter.com/mgrouchy).

Edit: Discussion on [Hacker News](http://news.ycombinator.com/item?id=3949774)
