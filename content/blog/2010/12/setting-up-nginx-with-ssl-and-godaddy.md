title: Setting up SSL with Nginx and Godaddy
author: Mike Grouchy
Date: 2010-12-14 18:07:00
tags:
    - ssl
    - nginx
    - godaddy

I was at a local coffee company the other day and [Josh](http://twitter.com/jlgosse)
and I were talking about some annoyances when dealing with godaddys SSL certificates.
 Talking to him about this reminded me that I had this post in the pipe for a long
 time and gave me the motivation to finish this.

On Many browsers, if you set up a standard Godaddy SSL Certificate out of the box,
 you will get ssl errors in many browsers saying that they can't recognize your
 certificate authority, this is generally not a good thing the whole point of installing
 SSL is for security and establishing trust iwith your customers, clients and website
 visitors.

To start the process of getting set up with an SSL certificate from godaddy just go
 and purchase one. You can pick anyone you like, but in general for most things you
 can get away with just purchasing the cheapest one, I think its around 21$/yr.

After you purchase your certificate, open up a terminal and log onto your server.
 You first need to create a key and certificate request for your domain.
<script src="http://gist.github.com/524908.js?file=gistfile1.sh"></script>

Just fill out the requested information and you should be good to go. You then log
 into your godaddy account and provide godaddy with the certificate request and they
 will generate the certificate for you. With the cheaper certificate this process usually
 takes minutes. For the more expensive certificte the process takes considerably longer.

After you recieve your certificates from godaddy, you need to put your certificates
 on your server and then you just add these lines to the approprate section of your
 configs depending on your webserver.

For nginx:
<script src="http://gist.github.com/524908.js?file=gistfile2.sh"></script>

For apache:
<script src="http://gist.github.com/524908.js?file=gistfile3.sh"></script>


If you have any questions, either leave something in the comments, or you can catch me [here on twitter](http://twitter.com/mgrouchy).


