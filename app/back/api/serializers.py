from rest_framework import serializers
from .models import CSVFile


class CSVFileSerializer(serializers.ModelSerializer):
  """
  Serializer for CSVFile model.

  This serializer is used to convert CSVFile model instances into JSON format
  and vice versa, facilitating the interaction between CSVFile objects and the
  RESTful API endpoints.
  
  Args:
    serializers (module): Module providing serialization capabilities.

  Attributes:
    model (Model): The model class to be serialized.
    exclude (list): List of model fields to be excluded from serialization.
  """
  class Meta:
    model = CSVFile
    exclude = ['uploaded']