#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Mike Grouchy'
AUTHOR_EMAIL = 'mgrouchy@gmail.com'
SITENAME = u'Mike Grouchy'

SITEURL = 'http://example.com:8000/'
RELATIVE_URLS = False

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

#Social widget
SOCIAL = (('@mgrouchy', 'http://twitter.com/mgrouchy'),
          ('mgrouchy on GitHub', 'http://github.com/mgrouchy'),)

DEFAULT_PAGINATION = 15
WEBASSETS = True

THEME = "dinky-pelican"
# syte settings
ABOUT = u''
SITE_DESCRIPTION = u''
SITE_KEYWORDS = u''

GOOGLE_PLUSONE = True

GITHUB_INTEGRATION_ENABLED = True
GITHUB_USERNAME = 'mgrouchy'
GRAVATAR = "mgrouchy@gmail.com"
EMAIL = "mgrouchy@gmail.com"
DISQUS_SITENAME = "mikegrouchy"

TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'mgrouchy'

# other settings
SUMMARY_MAX_LENGTH = None
COPYRIGHT_YEARS = "2008-2013"

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
BIO = "Ambitious Python Developer, Beer drinker and lover of all things basketball."

TEMPLATE_PAGES = {
    'override-content/be-pythonic-initpy.html': 'blog/be-pythonic-initpy.html',
    'override-content/compile-vim-with-python-on-osx-with-homebrew.html': 'blog/compile-vim-with-python-on-osx-with-homebrew.html',
    'override-content/zsh-is-your-friend.html': 'blog/zsh-is-your-friend.html',
    'override-content/introducing-pycoders-weekly.html': 'blog//introducing-pycoders-weekly.html',
    'CNAME': 'CNAME',
}
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

SITEMAP = {
    'format': 'xml',
}
