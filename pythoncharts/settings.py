"""
Django settings for pythoncharts project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4zp9l#qndnmsxiz+qhd37*lu24q63p94a#@zy-ny_1#m2#bl*x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','*.spmreportautomation.com','www.spmreportautomation.com','http://spmreportautomation.com','https://web-production-402f.up.railway.app', 'http://www.spmreportautomation.com']
#CSRF_TRUSTED_ORIGINS = ['*','*.spmreportautomation.com','www.spmreportautomation.com','http://spmreportautomation.com','https://web-production-402f.up.railway.app','http://www.spmreportautomation.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

#AUTH_USER_MODEL = 'auth.User'

#AUTH_USER_MODEL = 'spm.CustomUser'

# Application definition
"""DATABASE_URL = 'postgres://fksdtzbhxvswno:e671f9ba485695a923ddf137a26bc2408fe752d898c6544b2749d9a7a0a86f7b@ec2-52-44-13-158.compute-1.amazonaws.com:5432/d41k6lcpq0g7t9'
DATABASES = {
    'default':dj_database_url.config(default=DATABASE_URL)
}
"""


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pythoncharts',
    'spm',
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'pythoncharts.urls'

AUTH_USER_MODEL = 'spm.User'

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

WSGI_APPLICATION = 'pythoncharts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#somechart/chartspm
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddphqri2bfce6j',
        'USER': 'cpqoswecxbgycm',
        'PASSWORD': 'a62180ef8ccf04f3782366b3ff2a670b5cd915ba9c22132a24d8531c3d3a38e9',
        'HOST': 'ec2-54-211-255-161.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
#spmreport/spmreport
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6fkahkl62o0v3',
        'USER': 'rnfhgyczhkcfjj',
        'PASSWORD': 'ce8e0d7e7410d3938eb2fb66a2bd988ed9e3281b9aab8ee1470af2420b734206',
        'HOST': 'ec2-44-209-158-64.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}



#crunchy bridge/spmreport

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'uzfhocix',
        'USER': 'uzfhocix',
        'PASSWORD': 'PnvMzNA8eGixbJoBmY1HdgznrN1EXRLH',
        'HOST': 'babar.db.elephantsql.com',
        
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
#STATICFILES_DIRS  = [(os.path.join(BASE_DIR, 'static','spm'))]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
LOGIN_URL = 'login/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


#django_heroku.settings(locals())





