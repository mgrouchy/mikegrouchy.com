title: Force websites to use SSL in Google Chrome
author: Mike Grouchy
date: 2012-07-23 9:30:00
tags:
    - browser
    - security
    - tip

I saw this tip in the comments over at [Hacker News](http://news.ycombinator.com) today
and I thought that this is a great alternative to force SSL for sites that don't have
it available.

##Step 1
Navigate to Chrome's net internals dashboard by typing

`chrome://net-internals/` into your browser.

You should see:

![net-internals](/static/images/2012/07/net-internals.png)

##Step 2
Navigate to the [HSTS](http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)(HTTPS Strict Transport Security) Tab and you should see this:

![hsts](/static/images/2012/07/hsts.png)

##Step 3
From there its pretty easy, just type in the site you want to force to SSL and
you are done!

![hsts](/static/images/2012/07/add-hsts-domain.png)


Do you have any other Chrome security tips? Leave them in the comments!

