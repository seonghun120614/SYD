from django.urls import path, include
from django.conf.urls.static import static

from .env import *

urlpatterns = [
    path('', include('api.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)