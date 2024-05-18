from django.http import QueryDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import TestModel
from api.serializers import TestSerializer
import json


@api_view(['GET'])
def getData(request):
  test_table = TestModel.objects.all()
  serializer = TestSerializer(test_table, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def addData(request):
  if isinstance(request.data, QueryDict) and '_content' in request.data:
    data = json.loads(request.data['_content'])
  else:
    data = request.data
  
  serializer = TestSerializer(data=data)
  
  if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)