"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zcf2dsz4-1w#02i@xp%d@rq2r84g1(($13f-+v((7+$^mcx6r2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

FORCE_SESSION_TO_ONE=False
FORCE_INACTIVEUSER_ENDSESSION=False


STRIPE_SECRET_KEY='sk_test_ZP7A7uDCNapWFDAj0MFwejdR'
STRIPE_PUB_KEY='pk_test_OHADWNQQHJbzdqNAMtlMYOjo'

MAILCHIMP_API_KEY="86440f7c12d2e074652b3957e8a1afcc-us17"
MAILCHIMP_DATA_CENTER="us17"
MAILCHIMP_EMAIL_LIST_ID="91a3c56c97"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party
    'storages',
    #our apps
    'products',
    'search',
    'tags',
    'carts',
    'orders',
    'accounts',
    'billing',
    'addresses',
    'analytics',
    'marketing',
]

AUTH_USER_MODEL='accounts.User'

LOGIN_URL='/login/'
LOGIN_REDIRECT_UTL='/'
LOGOUT_URL='/logout/'
LOGOUT_REDIRECT_URL='/login/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static_my_proj')
]
STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),'static_cdn','static_root')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),'static_cdn','media_root')

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

AWS_GROUP_NAME='PAGNN_eCommerce_Group'
AWS_USERNAME='pagnn-ecommerce-user'
AWS_ACCESS_KEY_ID='AKIAJRUA6OMI25U7UKWA'
AWS_SECRET_KEY='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'