title: Embeddable Tweets
author: Mike Grouchy
Date: 2010-05-05 2:14:00
tags:
    - twitter
    - embed

Twitter now allows you to Embed a Tweet, all you need is the url of a tweet, like
[http://twitter.com/mgrouchy/status/13429079254](http://twitter.com/mgrouchy/status/13429079254),
and you can use Twitters [Blackbird Pie](http://media.twitter.com/blackbird-pie/
app to embed the tweet in your website like below:

<!-- http://twitter.com/mgrouchy/status/13429079254 --> <style type='text/css'>.bbpBox{background:url(http://s.twimg.com/a/1271891196/images/themes/theme15/bg.png) #022330;padding:20px;}p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px}p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6}p.bbpTweet span.metadata span.author{line-height:19px}p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px}p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox'><p class='bbpTweet'>This is me tweeting about how you can embed tweets, is this embedded?<span class='timestamp'><a title='Wed May 05 14:23:55 +0000 2010' href='http://twitter.com/mgrouchy/status/13429079254'>less than a minute ago</a> via <a href="http://www.tweetdeck.com" rel="nofollow">TweetDeck</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/mgrouchy'><img src='http://a3.twimg.com/profile_images/817183015/swix-hipster_normal.JPG' /></a><strong><a href='http://twitter.com/mgrouchy'>Mike Grouchy</a></strong><br/>mgrouchy</span></span></p></div> <!-- end of tweet -->

Here is the Source:

<script src="http://gist.github.com/390841.js"></script>

Its kind of interesting, Blackbird Pie just generates a html/css snippet that you
 can embed in your page. I am not sure if I prefer this way of doing things or the
 way [github](http://github.com) does it with cross site javascript.

What do you think?

