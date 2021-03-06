title: Great Python/Django Testing Talks
author: Mike Grouchy
Date: 2012-06-10 21:05:00
tags:
    - django
    - python
    - test
    - testing

I have been working on some tests for an upcoming product at [SWIX](http://swixhq.com)
and as any good developer I think its important to make an effort to constantly be
learning new things. In this vein I starting digging through the videos for
this years [Pycon US](https://us.pycon.org/2012/). Lo and Behold Testing was a
popular topic at Pycon so there were lots of talks to watch!


My two favorite talks were Testing and Django by [Carl Meyer](https://twitter.com/carljm)
and Fast Test, Slow Test by the always insightful [Gary Bernhardt](https://twitter.com/garybernhardt).

##Testing and Django - Carl Meyer
<iframe width="600" height="450" src="http://www.youtube.com/embed/ickNQcNXiS4" frameborder="0" allowfullscreen></iframe>
<br/>
Carl Meyer gives this great deep dive into testing Django projects, there are
plenty of gems in here, including some code for a Django Test Runner using Unittest2's
test discovery. Carl gives some great tips for writing tests with Django as well as tips
for just writing good tests in general.


##Fast Test, Slow Test - Gary Bernhardt
<iframe width="600" height="450" src="http://www.youtube.com/embed/RAxiiRPHS9k" frameborder="0" allowfullscreen></iframe>
<br/>
This talk is superb. Gary Bernhardt talks about how to write a fast test suite as
well as how you should be testing your applications. He points out that the slow
test suite problem is usually releated to the problem of test authors writing Unit
Tests which are actually System Tests.


Those two testing talks were my favorites, but some other good ones that are
worth checking out are:

* [Certainty in an Uncertain World: Gaining Confidence through Security Testing](http://www.youtube.com/watch?v=TmuEDxX1FDQ) - Geremy Condra
* [Fake It Til You Make It: Unit Testing Patterns With Mocks and Fakes](https://www.youtube.com/watch?v=hvPYuqzTPIk) - Brian K. Jones
* [Speedily Practical Large-Scale Tests](https://www.youtube.com/watch?v=1VZfL9JVgFg) - Erik Rose
* [Stop Mocking, Start Testing](https://www.youtube.com/watch?v=Xu5EhKVZdV8) - Augie Fackler & Nathaniel Manista
* [pytest - rapid and simple testing with Python](https://www.youtube.com/watch?v=9LVqBQcFmyw) - Holger Krekel

Besides these videos another great resource to take your Python testing a bit
farther is this book, the [Python Testing Cookbook ](http://amzn.to/LUe8SX). It
has plenty of great strategys that you can use for testing your Python projects.

If you have any other good Django testing tips or Talks leave them in the comments.
If you are looking for more Python news, tips and discussion you should check out
[Pycoders Weekly](http://pycoders.com), a weekly Python newsletter that I curate.
