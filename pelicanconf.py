#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Keith Gray'
SITENAME = u"Keith's Blog"
SITEURL = 'http://idahogray.github.io/blog'
#RELATIVE_URLS = True

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (
          ('POWER Engineers', 'http://www.powereng.com'),
          ('Python.org', 'http://python.org'),
          ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/idahogray'),
          ('github', 'http://github.com/idahogray'),)

DEFAULT_PAGINATION = 10

THEME = '../pelican-themes/bootstrap'
DISQUS_SITENAME = 'keithgraysblog'
GITHUB_URL = 'http://github.com/idahogray/'

FEED_DOMAIN = 'http://idahogray.github.com'
FEED_RSS = 'feeds/rss.xml'

STATIC_PATHS = ["images", ]
PATH = 'content'
