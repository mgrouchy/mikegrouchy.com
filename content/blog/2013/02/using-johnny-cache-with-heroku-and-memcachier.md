title: Using Johnny Cache with Heroku and Memcachier
author: Mike Grouchy
date: 2013-02-21 20:25:00
tags:
    - python
    - django
    - johnny-cache
    - libmemcached
    - memcached
    - SASL

[Johnny Cache](https://github.com/jmoiron/johnny-cache) is a pretty great caching framework for Django.
For most apps you can drop Johnny-cache in and depending on your Django project get
a good result right out of the box. If this sounds appealing check out the [docs](http://pythonhosted.org/johnny-cache/)
for more details.

A recent issue that I have run into is that a deploying a Django App on [Heroku](http://heroku.com) with
Johnny Cache does not work out of the box with my [Memcached](http://memcached.org/) service
of choice [Memcachier](http://www.memcachier.com/).

After some investigation the issue here is that Johnny Cache doesn't support
[SASL](http://en.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer) out of the box which is how the authentication for Memcachier works.
Memcachier reccomends using [django-pylibmc's](https://github.com/jbalogh/django-pylibmc)
[libmemcached](http://libmemcached.org/libMemcached.html) backend to use its app.
Of course this isn't compatible with Johnny Cache out of the box either so what do you do?

##Create your own SASL compatible backend for Johnny Cache

This is a fairly straightforward problem to solve, we can just inherit from the
`PyLibMCCache` backend from django-pylibmc and override its `_get_memcache_timeout`
method with the one from Johnny Cache.

Then update your django settings file to point at the new backend you have just
created.

<script src="https://gist.github.com/mgrouchy/4956137.js"></script>

Make sure in your CACHES settings dict that you make sure you set BINARY to True
and you are off to the races.

Any questions? Feel free to ask in the comments or hit me up on [Twitter](http://twitter.com/mgrouchy)
