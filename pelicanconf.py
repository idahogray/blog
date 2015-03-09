#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Keith Gray'
SITENAME = "Keith's Blog"
SITEURL = 'http://idahogray.github.io/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('POWER Engineers', 'http://www.powereng.com'),
    ('Python.org', 'http://python.org'),
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Jinja2', 'http://jinja.pocoo.org'),
)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/idahogray'),
          ('github', 'http://github.com/idahogray'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'bootstrap'
DISQUS_SITENAME = 'keithgraysblog'
GITHUB_URL = 'http://github.com/idahogray/'

FEED_DOMAIN = 'http://idahogray.github.com'
FEED_RSS = 'feeds/rss.xml'

STATIC_PATHS = ["images", ]
PATH = 'content'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
