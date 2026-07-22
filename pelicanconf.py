from datetime import datetime

AUTHOR = 'Bob King'
SITENAME = 'Ready-1'
SITESUBTITLE = 'Broadcast engineering for corporate live events'
SITEDESCRIPTION = 'Broadcast engineering for corporate live events, including multi-camera systems, signal routing, networking, control, and image matching.'
SITEURL = ''

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['pdfs', 'images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/.nojekyll': {'path': '.nojekyll'},
}
# ARTICLE_PATHS = ['articles']

DEFAULT_PAGINATION = 10
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.7,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly',
    },
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_DATE_FORMAT = '%B %-d, %Y'

THEME = 'themes/pelican-bootstrap-5'
THEME__BOOTSWATCH = 'darkly'

DEFAULT_SOCIAL_IMAGE = 'nobe-chroma-du-monde.png'

COPYRIGHT_YEAR = datetime.now().year
