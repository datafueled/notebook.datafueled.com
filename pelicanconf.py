#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bruce Mitchener, Jr.'
SITENAME = u"Bruce's Notebook"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ArmyOfBruce'),
          ('Github', 'https://github.com/waywardmonkeys'),
          ('GitTip', 'https://gratipay.com/waywardmonkeys/'),
          ('Email', 'mailto:bruce.mitchener@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search',
           'neighbors', 'related_posts', 'share_post',
           'multi_part']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


THEME = 'themes/elegant'

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
