from django.urls import path
from .views import FileUplaodAPIView


urlpatterns = [
  path('upload', FileUplaodAPIView.as_view(), name="upload")
]