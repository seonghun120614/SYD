from .base import *

DEBUG = False
ALLOWED_HOSTS = [ "*" ]

CORS_ALLOWED_ORIGINS = (
  'http://0.0.0.0:8080',
)

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True
    }
}