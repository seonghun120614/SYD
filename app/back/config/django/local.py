from .base import *

DEBUG = True
ALLOWED_HOSTS = [ "*" ]

# Allow Hosts for Cross-origin resource sharing
CORS_ALLOWED_ORIGINS = (
  'http://localhost:5173',
  'http://localhost:3000'
)