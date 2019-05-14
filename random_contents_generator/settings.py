"""
Django settings for random_contents_generator project.
"""

import os
import json


with open('environments/settings.json') as f:
    environment = json.loads(f.read())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = environment['secret_key']
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'random_contents_generator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'random_contents_generator.wsgi.application'

database = environment['database']
if database['type'] is 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': database['engine'],
            'NAME': database['name'],
            'USER': database['user'],
            'PASSWORD': database['password'],
            'HOST': database['host'],
            'PORT': database['port']
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = environment['static']['static_url']
STATIC_ROOT = environment['static']['static_root']
MEDIA_URL = environment['media']['media_url']
MEDIA_ROOT = environment['media']['media_root']

ATTACH_EXTENSIONS = ['hwp', 'xls', 'xlsx', 'doc', 'docx', 'ppt', 'pptx', 'pdf']
ATTACH_FILES = environment['attaches']

COPYRIGHT_TEXT = '©Copyright 2019, HwangJongtaek'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 365  # One year

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'request': {
            'format': '[%(levelname)s]|%(asctime)s|%(pathname)s|%(lineno)s|'
                      '%(funcName)s()|%(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'request'
        },
        'log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './log/'
                        'debug.log',
            'formatter': 'request'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './log/'
                        'info.log',
            'formatter': 'request'
        },
    },
    'loggers': {
        'api': {
            'handlers': ['log', 'info', 'console'],
            'level': 'DEBUG'
        },
        'core': {
            'handlers': ['log', 'info', 'console'],
            'level': 'DEBUG'
        }
    }
}
