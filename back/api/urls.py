from django.urls import path
from .views import CSVFileAPIView


urlpatterns = [
  path('upload', CSVFileAPIView.as_view(), name="csv-file-api")
]