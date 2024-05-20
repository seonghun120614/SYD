from django.urls import path
from .views import CSVFileAPIView


urlpatterns = [
  path('csv_files/', CSVFileAPIView.as_view())
]