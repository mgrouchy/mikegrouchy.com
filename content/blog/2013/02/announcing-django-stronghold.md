title: Announcing Django-Stronghold
author: Mike Grouchy
date: 2013-02-15 10:00:00
tags:
    - python
    - django
    - authentication

I spent much of last year trying to turn up my open source contributions
so I spent much of my time contributing to other peoples open source projects. Its
2013 and its a new year, so I am making a push to get some open source projects
that I have had in the pipe actually out there in the wild.

The first of these is [django-stronghold](http://github.com/mgrouchy/django-stronghold).

If you are a Django developer and
you have worked on a Django project of any size, you might have coded something
like this already which makes it the perfect target for open source.

Stronghold defaults your Django project to private. This means that via
some middleware all your Django views become `login_required`. Stronghold also
provides some mechanisims to make views public via a decorator or whitelisting
some of your url patterns. If this sounds useful to you [check it out](http://github.com/mgrouchy/django-stronghold). If you run into any issues please let me know!

Shout out to [Richard Blair](http://twitter.com/richardlblair) for help with this.
