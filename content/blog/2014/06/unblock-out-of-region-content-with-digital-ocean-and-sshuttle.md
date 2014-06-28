title: Unblock out of region content with Digital Ocean and sshuttle
author: Mike Grouchy
date: 2014-06-22
tags:
    - python
    - DNS
    - Digital Ocean
	- sshuttle


If you live in Canada(like me) or elsewhere. You are probably interested in
paying for services like Hulu and Spotify and are probably wondering how you
can get that good US netflix content. You will be happy to know that it is in
fact very easy to accomplish this for as little as 5$/month through Digital
Ocean and still have a server that you can do other things with in the meantime.

Before I go through the setup here, I know there are alternatives which are
similarily priced. Unblock.us, and mediahint to just name a couple.The big
advantage here is that you can setup/teardown your Digital Ocean droplets at
your convenience which is nice if you are really pinching pennies, because
these are charged hourly.

!["Digital Ocean Pricing"](/static/images/2014/digital-ocean-pricing.png)

The other big advantage of using something like Digital Ocean is that you can
use the droplet for other things besides using it tunnel your internet traffic.
Convinced yet? If so, lets move on to the setup.

##1. Signup For Digital Ocean/Set up a Droplet
The first step here is just to head over to [Digital Ocean](https://www.digitalocean.com/?refcode=b0a3d514963a) (referral) and signup. This can
also be accomplished with a VPN you already have, and if that is the route you
want to go, just head on down to step 2.

Once you have logged into your [Digital Ocean](https://www.digitalocean.com/?refcode=b0a3d514963a) account and have verified your email
and billing details you can go ahead and click on the "Create" button in the
side bar. This should give you the Droplet creation wizard and you can just follow
these steps:

First chose a hostname, this can be whatever you want, like "VPN", etc.
!["Choose Hostname"](/static/images/2014/creat-droplet-hostname.png)
Once you have chosen a hostname, go ahead and select the region you want your
traffic to be in. If you are Canadian like me who might want your traffic to
appear as it is comign from the US then you want to select a US Region.
!["Select Region"](/static/images/2014/digital-ocean-select-region.png)
Next you choose your flavor of Linux, in my case I have chosen Ubuntu.
!["Select Droplet Image"](/static/images/2014/digital-ocean-select-image.png)
Next you want to choose the SSH keys to use, if you have [set them up](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2).
If you don't have ssh keys set up and you don't want to use them. That is okay,
after you create the droplet [Digital Ocean](https://www.digitalocean.com/?refcode=b0a3d514963a) will email you a root password to the
email you signed up with. It is recommended you change this root password by sshing
into your droplet with the current root password and [changing it](https://www.digitalocean.com/community/questions/can-i-change-root-password).
!["Choose SSH Keys and Create"](/static/images/2014/digital-ocean-ssh-create.png)

##2. Install sshuttle
Installing sshuttle is each, just download it to your computer. You also need Python installed on
your machine(Mac or Linux) to eventually run sshuttle.

```shell
    git clone git://github.com/apenwarr/sshuttle
```

Optionally you can download and extract a `zip` or a `.tar.gz` from the sshuttle
[download page](https://github.com/apenwarr/sshuttle/releases) on [Github](http://github.com).
##3. Start your Tunnel
Okay. We have our droplet setup and we have downloaded sshuttle. Now to start
our DNS tunnel.

Navigate to the directory where you downloaded sshuttle locally then:

```shell
   ./sshuttle --dns -vvr root@dropletserver 0/0
```

This will then prompt you for your local root password and the password to your
droplet.
**Note**: On OSX this will require a restart after you run this the first time.

You should now be able to navigate to that out of region website you wanted to
visit so much and it should just work.

!["Hulu"](/static/images/2014/hulu.png)

## What else is this good for?

* It is essentially a poor mans instant VPN, you don't even need to have root access on the machine you are connecting to.
* Allows you to surf safely. It protects you from standard attacks like Firesheep on insecure networks.
* Anything else you can think of that you would like to use a VPN for.


Any other uses for this or thoughts about this? Leave something in the comments or
contact me on [twitter](http://twitter.com/mgrouchy).

