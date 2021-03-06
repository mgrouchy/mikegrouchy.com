title: Zsh is your friend
author: Mike Grouchy
Date: 2012-01-31 11:14:00
tags:
    - zsh
    - shell
    - terminal

I don't know if you know this, but ZShell is your friend, you might not know it
yet, but its true. I know what you are thinking , "whats wrong with Bash?",
nothing, except its not Zsh.

Its not that Bash is a bad guy, I don't want to put him down, but if we
were picking teams, Bash would be last picked in gym class.

He isn't very versatile and he doesn't do anything particularily great, all in all
he is kind of just a worse Zsh(or Zsh is kind of like a better Bash).

Zsh is easy to get started with because it looks and acts like bash in a lot of
ways. So if you are familiar with bash don't worry, you can try zsh out without
skipping a beat and you still end up with a better shell.

###Why is Zsh better than Bash?

In my mind one of the most important reasons why Zsh is better than bash is
autocompletion, and I don't mean that whimpy autocompletion you get by installing
bash completion. I mean, this is real deal command completion, besides getting all
the completion of common commands on the command line, and being ridiculously
fast, the completion also gives you a keyboard navigable completion list.

![zshcompletion](/static/images/2012/01/zshcompletion.jpg)

Okay, I know what you are saying, big deal right? Well how about really great built
in autocompletion for common commands. Lets use Kill as an example. You type

```
	Kill <tab>
```

in bash, you get what, the list of all files that are in your current
working directory. Not very helpful behavior in my opinion. What happens if you
type

```
	kill <tab>
```

in Zsh? This:

![zshkillcompletion](/static/images/2012/01/zshkillcompletion.jpg)

Lists of all your processes with pids? Yes please.

Another thing that make makes Zsh stand out is shared history. If you are anything
like me you live in the terminal all day long. There is nothing worse(I'm exaggerating)
than opening another terminal in a tab and navigating your history looking for
that recent thing you just did in another window and have it not be in your
history. In Zsh this isn't an issue.


###Time for more awesome

Okay, so we have great, fast autocompletion and shared history. How much more awesome
could there be? Lots!

Autocorrect is pretty cool

	mikegrouchyv2 ::(master*) » gut status
	zsh: correct 'gut' to 'git' [nyae]?y
	git status

Hey thats pretty cool, autocorrect for known commands. What would I do
without you(besides type the command again)?

Even cooler than autocorrect, for the super nerd(like me) Vi and emacs mode,
**shit yeah**, you can have your favorite editor on your command line. It will
support common movement commands and editing modes, like command and insert mode
for Vi.

Last but certianly not least, Zsh has [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
from the website:


> A community-driven framework for managing your zsh configuration. Includes 40+ optional plugins (rails, git, OSX, hub, capistrano, brew, ant, macports, etc), over 80 terminal themes to spice up your morning, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.

I know one exists for bash, but I find oh-my-zsh to be excellent, it autoupdates,
has great plugins and a very active community behind it.

All in all, Zsh is pretty great, so if you haven't tried Zsh, maybe its time you
try it out. If so [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) is a
pretty great place to start.

Also releated reading, a book that was reccomended to me with a lot of great
Zsh tips as well as Bash tips for those who I haven't convinced yet is [Bash to Z Shell: Conquering the Command Line](http://amzn.to/KkPrDo).

If you are already drinking the Kool-aid and have some Zsh tips to share, either
leave a comment or hit me up on [twitter](http://twitter.com/mgrouchy).

**EDIT**: If you are interested in learning more about Zsh, check out the [Zsh FAQ](http://zsh.sourceforge.net/FAQ/).
Its pretty complete and much better than I could do in a very basic blog post.

Also, [More discussion on Hacker News](http://news.ycombinator.com/item?id=3533895)
