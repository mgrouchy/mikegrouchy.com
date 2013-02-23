#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

PLUGINS=['pelican.plugins.sitemap',]

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

SITEURL = 'http://mikegrouchy.com/'


PLUGINS = [
    'pelican.plugins.assets',
    'pelican.plugins.gravatar',
    'pelican_gist',
]

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

DISQUS_SITENAME = "mikegrouchy"
GOOGLE_ANALYTICS = "UA-1990784-1"
