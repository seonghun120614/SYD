import os
from django.conf import settings
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import File
from .utils.frame import Frame


class FileUplaodAPIView(APIView):
    """
    API view for interacting with File objects.
    Provides endpoints for retrieving and creating File objects.
    """
  
    def get(self, request):
      """
      Retrieve all File objects.

      Returns:
          Response: A response containing serialized File objects.
      """
      
      csv_files = File.objects.all()
      serializer = FileSerializer(csv_files, many=True)
      
      return Response(serializer.data)
  
    def post(self, request):
        """
        Create a new File object.

        Args:
            request (Request): The HTTP request containing the data to create the File object.

        Returns:
            Response: A response containing the serialized File object if creation is successful,
            or errors if the provided data is invalid.
        """
        serializer = FileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

