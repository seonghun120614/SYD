from django.urls import path
from .views import CSVFileAPIView


urlpatterns = [
  path('api/', CSVFileAPIView.as_view())
]