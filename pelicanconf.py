#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adrian Espinosa'
SITENAME = u'Adrian Espinosa.'
SITEURL = ''
TAGLINE = 'Software Developer'
TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/aesptux'),
          ('Github', 'http://www.github.com/aesptux'),
          ('Email', 'mailto:aespinosamoreno@gmail.com'),
          ('LinkedIn', 'http://www.linkedin.com/in/aespinosamoreno/en'))
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/opt/aesptux.com/themes/svbhack"
#THEME = "theme"
#THEME = "/opt/tests/pelican/all_themes/storm"
FOOTER_TEXT='Adrian Espinosa Moreno.'

GOOGLE_ANALYTICS = 'UA-24400876-1'

DISQUS_SITENAME = 'aesptuxblog'

INTERNET_DEFENSE_LEAGUE = True
