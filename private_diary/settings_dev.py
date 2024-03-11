from .settings_common import *



SECRET_KEY = 'django-insecure-44h4nrj=m8412maj$4ue007pod1t7g)@+j-en)u!)h@zo^!*9p'

DEBUG = True

ALLOWED_HOSTS = []

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/static'

LOGGING={
    'version':1,
    'disable_existing_loggers':False,

    'logger':{

        'django':{
            'handlers':['console'],
            'level':'INFO',
        },

        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')