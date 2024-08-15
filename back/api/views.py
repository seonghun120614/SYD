import os
from django.conf import settings
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CSVFileSerializer
from .models import CSVFile
from .utils.frame import Frame


class CSVFileAPIView(APIView):
    """
    API view for interacting with CSVFile objects.
    Provides endpoints for retrieving and creating CSVFile objects.
    """
  
    def get(self, request):
      """
      Retrieve all CSVFile objects.

      Returns:
          Response: A response containing serialized CSVFile objects.
      """
      
      csv_files = CSVFile.objects.all()
      serializer = CSVFileSerializer(csv_files, many=True)
      
      return Response(serializer.data)
  
    def post(self, request):
        """
        Create a new CSVFile object.

        Args:
            request (Request): The HTTP request containing the data to create the CSVFile object.

        Returns:
            Response: A response containing the serialized CSVFile object if creation is successful,
            or errors if the provided data is invalid.
        """
        serializer = CSVFileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            # Generate binary strings for the uploaded CSV file
            title = serializer.validated_data['title']
            f = Frame(os.path.join(settings.MEDIA_ROOT, title+'.csv'))
            
            binary_strings = f.get_binary_strings()  # Generate binary strings

            return Response(binary_strings, status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)