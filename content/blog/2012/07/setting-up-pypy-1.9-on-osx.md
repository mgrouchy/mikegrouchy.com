title: Setting up PyPy 1.9 on OSX
author: Mike Grouchy
date: 2012-07-08 10:00:00
tags:
    - software
    - programming
    - pypy
    - python

![pypy](http://pypy.org/image/pypy-logo.png)

As I had said before on [this](http://mikegrouchy.com/blog/setting-up-nginx-with-ssl-and-godaddy.html) [blog](http://mikegrouchy.com/blog/great-django-test-talks.html), I sometimes use it as a way to record things I want to remember. This is one of those times.

I have started a new project that uses PyPy and while there is documentation out there to get started, I find it useful to have it all in the same place and not spread around.

##What is PyPy
PyPy is Python interpreter and JIT compiler. The latest PyPy release PyPy 1.9, the one we are installing, is CPython 2.7.2 compatible. PyPy is focused on speed and 100% compatibility with the [CPython](http://en.wikipedia.org/wiki/CPython).

##Installing PyPy
There are a couple of options to install PyPy on OSX.

* You can install using the [binary](https://bitbucket.org/pypy/pypy/downloads/pypy-1.9-osx64.tar.bz2) from the PyPy website.
* You can [build PyPy from source](http://pypy.org/download.html#building-from-source).
* You can install using [Homebrew](http://mxcl.github.com/homebrew/).

I like to manage my packages using Homebrew when thats an option, so I installed using Homebrew.
It was very easy to get setup just

```sh
	brew install PyPy
```

Then follow any instructions in your terminal.

You should then see a symlink in your /usr/local/bin directory for PyPy

```sh
	~ >> ls /usr/local/bin | grep pypy
	pypy
```

And assuming you have homebrew setup correctly you should be able to type "pypy" in your terminal and get an interactive interpreter.

```sh
	~ >> pypy
	Python 2.7.2 (341e1e3821ff, Jun 07 2012, 15:42:54)
	[PyPy 1.9.0 with GCC 4.2.1] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	And now for something completely different: ``it's beautiful: very rectangular
	and yellow''
	>>>>
```

If you have gotten this far you have been successful at installing PyPy!

Now, like any good [pycoder](http://pycoders.com), lets move on to getting PyPy setup inside a Virtualenv.


##Getting PyPy to work with Virtualenv or Virtualenvwrapper
Luckily getting PyPy set up in a virtualenv is really easy, for virtualenv the command is:

```sh
	virtualenv -p /usr/local/bin/pypy environmentname
```

for Virtualenvwrapper, its basically the same:

```sh
	mkvirtualenv -p /usr/local/bin/pypy environmentname
```

In the output of each of these commands you should see:

```sh
	Running virtualenv with interpreter /usr/local/bin/pypy
	New pypy executable in testpypy2/bin/pypy
	Installing setuptools............done.
	Installing pip...............done.
```

Now you can activate your environment.

In virtualenv:

```sh
	source /path/to/your/virtualenv/bin/activate
```

In [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/):

```sh
	workon environmentname
```

And test your Python version:

```sh
	python --version
	Python 2.7.2 (341e1e3821ff, Jun 07 2012, 15:42:54)
	[PyPy 1.9.0 with GCC 4.2.1]
```

Now you are good to get working on your Python project with PyPy. Happy hacking!
