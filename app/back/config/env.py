import environ
import os


# Get environmental variables
env = environ.Env()

# Setup Root and Apps Directory
BASE_DIR = APPS_DIR = environ.Path(__file__) - 2

# Setup Media Directory
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# Setup root url config
ROOT_URLCONF = 'config.urls'

# Take variables where in .env file
environ.Env().read_env(os.path.join(BASE_DIR, '.env'))

# Get SECRET_KEY
SECRET_KEY = env('SECRET_KEY')

