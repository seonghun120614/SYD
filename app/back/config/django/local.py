from .base import *

DEBUG = True
ALLOWED_HOSTS = [ "*" ]

CORS_ORIGIN_WHITELIST = (
  'http://127.0.0.1:8000',
  'http://localhost:3000',
  'http://localhost:5173'
)

CORS_ALLOW_CREDENTIALS = True