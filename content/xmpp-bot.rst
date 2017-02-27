XMPP Bot File Transfer
======================

:date: 2014-06-21
:tags: python xmpp programming
:category: work
:summary: I spent a few days figuring out how to transfer a file using a XMPP
          bot
:status: draft

Purpose
-------

I have set up a XMPP server at work. People from all over our business unit use
the server to chat with each other. I have been thinking about writing a bot
to help automate some tasks. One of the first tasks I wanted to automate was
getting a project's status report from our intranet. I am imagining that a user
would send the project number to the bot, the bot would download the report,
the bot would then use XMPP to transfer the file to the user.

Tools
-----

I have been doing a bit of Python programming over the last few years and I 
wanted to write the bot in Python. A few of the libraries I looked at did not
support file transfer and I eventually settled on the `SleekXMPP`_ library. The
server is running `ejabberd`_. Most, if not all, of the users are running
`Pidgin`_ as their XMPP client.

First Try
---------

After doing some initial research, I determined that there were two ways to
do file transfer with XMPP. The first was in-band bytestreams (ibb) (XEP-0047).
The second method was SOCKS5 bytestreams (XEP-0065).

IBB appeared to be the easier of the two methods even with the understanding
that ibb was intended for small transfers. I decided to give ibb a shot.

EchoBot
~~~~~~~

I first built the example in the SleekXMPP README file. It is called EchoBot.
The bot connects to the server and echos back everything that is said to it.
The only thing I had to change in order for it to work with my set up was to 
pass the server IP and TCP port as a tuple to the connect() method.

The source for this first version of `EchoBot`_ is hosted at bitbucket.org.

IBB
~~~

Once I was able to successfully connect to the server, receive messages, and
send messages I attempted file transfer.


.. _SleekXMPP: https://github.com/fritzy/SleekXMPP
.. _ejabberd: http://www.ejabberd.im/
.. _Pidgin: https://pidgin.im/
.. _EchoBot: https://bitbucket.org/idahogray/xmpp-bot/src/bb92bc4f6808f8d5c381e7ef6df77e2379cd98a4/xmpp_bot/echo_bot.py?at=default
