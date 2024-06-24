from .base import *

DEBUG = True
ALLOWED_HOSTS = [ "*" ]
SECRET_KEY = "afidz$4l_e$&p#9-(ago-e4=38(@=za(aaik=qbmg4i4u=eap)"

CORS_ALLOWED_ORIGINS = (
  'http://0.0.0.0:5173',
)

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True
    }
}