import environ
import os


env = environ.Env()

APPS_DIR = BASE_DIR = environ.Path(__file__) - 2
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

environ.Env().read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY', default="t*&i$9@452mcsqp%ud8s8@!yrh^f!wr9_n)j!&z0978!=_nu-a")