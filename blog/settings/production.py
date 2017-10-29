from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'personal_blog_db',
        'USER': 'jason_blog',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}