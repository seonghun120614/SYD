from .base import *

DEBUG = False
ALLOWED_HOSTS = [ "*" ]

CORS_ALLOWED_ORIGINS = (
    'http://0.0.0.0:8080',
    'http://0.0.0.0:80',
    'http://localhost:8080',
    'http://localhost:80',
    'http://syd-front:8080',
    'http://syd-front:80',
)

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True
    }
}