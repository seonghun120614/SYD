import environ
import os

# Setup Root and Apps Directory
BASE_DIR = APPS_DIR = environ.Path(__file__) - 2

# Setup Media Directory
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Setup root url config
ROOT_URLCONF = 'config.urls'

# Take variables where in .env file
environ.Env().read_env(os.path.join(BASE_DIR, '.env'))