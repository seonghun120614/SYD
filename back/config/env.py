import environ
import os

# Setup Root and Apps Directory

env = environ.Env(
    DEBUG=(bool, True)
)

BASE_DIR = APPS_DIR = environ.Path(__file__) - 2

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env('DEBUG')

SECRET_KEY = env.str('SECRET_KEY')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ROOT_URLCONF = 'config.urls'