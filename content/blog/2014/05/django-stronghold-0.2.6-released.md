title: Django-Stronghold 0.2.6 released
author: Mike Grouchy
date: 2014-05-28
tags:
    - python
    - django
    - stronghold

I have just pushed version 0.2.6 of [Django-Stronghold](https://github.com/mgrouchy/django-stronghold) to [pypi](https://pypi.python.org/pypi/django-stronghold/).

The main update in this version is the new configuration option `STRONGHOLD_PERMISSIONS_DECORATOR`.

The STRONGHOLD_PERMISSIONS_DECORATOR setting allows you to override the default
behavior which currently defaults to requiring your views to default to
login_required and replace that with any decorator you like that serves your
purpose like the `staff_member_required decorator` or a decorator you have created
yourself which supports your specific mix of login requirements.

This version currently supports Django 1.4.x, 1.5.x and 1.6.x, download it and
try it out and please [report any bugs](https://github.com/mgrouchy/django-stronghold/issues) if you notice anything.
