from .base import * #NOQA



DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scribbles_db',
        'USER':'root',
        'PASSWORD':'****',
        'HOST':'127.0.0.1',
        'PORT':3306,
        #'CONN_MAX_AGE':5*60,
        #'OPTIONS':{'charset':'utf8mb4'}
    }
}




INSTALLED_APPS += [
    'debug_toolbar',
    # 'debug_toolbar_line_profiler',
    # 'silk',

]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

# INTERNAL_IPS = ['127.0.0.1']

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
# }

# DEBUG_TOOLBAR_PANELS = [
#     # 'djdt_flamegraph.FlamegraphPanel',
#     # 'debug_toolbar.panels.timer.TimerPanel',
#     # 'pympler.panels.MemoryPanel',
#     # 'debug_toolbar_line_profiler.panel.ProfilingPanel',

# ]