from rest_framework.status import (
  HTTP_200_OK,
  HTTP_201_CREATED,
  HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import CSVFileSerializer
from .models import CSVFile


class CSVFileAPIView(APIView):
  
  def get(self, request):
    serializer = CSVFileSerializer(CSVFile.objects.all(), many=True)
    return Response(serializer.data, status=HTTP_200_OK)
  
  
  def post(self, request):
    serializer = CSVFileSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    