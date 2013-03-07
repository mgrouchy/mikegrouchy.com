title: Yes, your code does need comments.
author: Mike Grouchy
date: 2013-03-05
tags:
    - software
	- programming

I imagine that this post is going to draw the ire of some. It seems like every
time I mention this on [Twitter](http://twitter.com/mgrouchy) or anywhere else
there is always some pushback from people who think that putting comments in
your code is a waste of time.

I think your code needs comments, but so we have a mutual understanding, lets
qualify that.

```python
def somefunction(a, b):
   #add a to b
   c = a + b
   #return the result of a + b
   return c
```

I understand this is a contrived example but this is the comment trap that new
developers get caught in. These types of comments really aren't useful to anyone.
Peppering the code that you just wrote with excessive comments, especially when
it is abundantly clear what the code is doing, is the least useful type of comment
you can write.

> "Code is far better describing what code does than English, so just write clear code"

This is usually the blowback you get from comments like the ones above. I don't
disagree, programming languages are definitely more precise then English. What I
don't agree with is the idea that if the code is clear and understandable that
comments are unneeded or don't have a place in modern software development.

So knowing this, what kind of comments am I advocating for? I'm advocating for
comments as documentation. Comments that explain what a complex piece of code
does, and most importantly what an entire function or Class does and why they
exist in the first place.

So what is a good example of the kind of documentation I am talking about? I
think [Zed Shaw's](http://twitter.com/zedshaw) [Lamson](http://github.com/zedshaw/lamson) is a fantastic example of this. Here is a code excerpt from that:

```python

class Relay(object):
    """
    Used to talk to your "relay server" or smart host, this is probably the most
    important class in the handlers next to the lamson.routing.Router.
    It supports a few simple operations for sending mail, replying, and can
    log the protocol it uses to stderr if you set debug=1 on __init__.
    """
    def __init__(self, host='127.0.0.1', port=25, username=None, password=None,
                 ssl=False, starttls=False, debug=0):
        """
        The hostname and port we're connecting to, and the debug level (default to 0).
        Optional username and password for smtp authentication.
        If ssl is True smtplib.SMTP_SSL will be used.
        If starttls is True (and ssl False), smtp connection will be put in TLS mode.
        It does the hard work of delivering messages to the relay host.
        """
        self.hostname = host
        self.port = port
        self.debug = debug
        self.username = username
        self.password = password
        self.ssl = ssl
        self.starttls = starttls

   ...

```
This code snippet is from [https://github.com/zedshaw/lamson/blob/master/lamson/server.py](https://github.com/zedshaw/lamson/blob/master/lamson/server.py). You can poke around the lamson code and see some good looking
Python code but also some usefully documented code.

##So hold on. Why are we writing comments?

Why are we writing comments, if you write clean, understandable code? Why do we
need to explain what classes and functions do if the code is "clear" and easy to
understand.

In my opinion, we write comments to capture intent. Comments are the only way
to capture the intent of the code at the time of writing.

Looking at a block of code only allows you to understand the intent of that
particular code at that moment in time which may be very different then the
intent of the code at time of its original writing.


##Writing comments captures intent.

Writing comments captures the original meaning of the code. Python has [docstrings](http://www.python.org/dev/peps/pep-0257/)
for this, other languages have comparable options. What is so good about docstring
type comments? In conjunction with unambiguous class and function names they can
easily describe the original intent of your code.

Why is capturing the original intent of your code important?

* It allows a developer, at a glance, to look at a piece of code and know why it exists.
* It reduces situations where a piece of codes original intent isn't clear then gets modified
and leads to unintended regressions.
* It reduces the amount of context a developer must hold his/her mind to solve any particular problem that may be contained in a piece of code.

**Writing comments to capture intent is like writing tests to prove that your software does what is expected.**

##Where do we go from here?

The first step is to realize that the documentation/comments accompanying a piece
of code can be just important as the code itself and need to be maintained as such.
Just like code can become stale if you don't keep it updated so do comments.
If you update some code you *must* update the accompanying comments/documentation
or they become useless and can lead to more developer error then not having comments
at all. So we have to treat comments and documentation as first class citizens.

Next we have to agree on what is important to comment on in your code, and how to
structure your code to make your use of comments most effective. Most of this
relies on your own judgement but we can cover most issues with some steadfast rules.

1. Never name your classes and functions ambiguously.
2. Always use inline comments on code blocks that are complicated or may appear unclear.
3. Always use descriptive variable names.
4. Always write comments describing the intent or reason why a piece of code exists.
5. Always keep comments up to date when editing commented code.


As you can see from the points above code as documentation and comments as documentation are not mutually exclusive. Both
are necessary to create readable code that is easily maintained by you and future maintainers.




> If you are interested in keeping up with the latest Python news, discussions,
> projects, articles and Jobs you should check out [Pycoder's Weekly](http://pycoders.com) the Python
> newsletter that I curate.
