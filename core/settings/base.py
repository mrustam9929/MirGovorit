import os
from pathlib import Path

# region DJANGO_SETTINGS
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'django-insecure-2e6%^=n+_n9a9t3!vl#95*d=-$^-(#^4v!#w1y0kuh#-fpau!*'
DEBUG = True
ALLOWED_HOSTS = []

DJANGO = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
APPS = [
    'apps.products',
]
LIBS = [
    'rest_framework',
    'drf_yasg',
]
INSTALLED_APPS = DJANGO + LIBS + APPS

WSGI_APPLICATION = 'core.wsgi.application'
ROOT_URLCONF = 'core.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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
# endregion

# region DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# endregion

# region MEDIA

MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR).joinpath('media')
STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR).joinpath('static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# endregion


# region INTERNATIONALIZATION
LANGUAGE_CODE = 'ru'
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
# endregion


# region REST_FRAMEWORK_SETTINGS
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}
    },
    'DEFAULT_MODEL_RENDERING': 'example'
}
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
# endregion
