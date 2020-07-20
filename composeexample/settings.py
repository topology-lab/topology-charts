from composeexample.base_settings import *

# 本番環境(heroku)
DEBUG = True
# loggerの設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
# DB設定
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

# Activate Django-Heroku.
import django_heroku
django_heroku.settings(locals())
