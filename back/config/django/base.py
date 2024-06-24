from config.env import *


# Application import
LOCAL_APPS = [
    'api'
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders'
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

# Middleware config
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]


# Template config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# Synchronous server config
WSGI_APPLICATION = 'config.wsgi.application'

# Password validation config
AUTH_PASSWORD_VALIDATORS = []


# Internationalization config
LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'