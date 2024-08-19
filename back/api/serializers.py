from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    """
    Serializer for File model.
    
    Meta:
        model (Model): The model class to be serialized.
        exclude (list): List of model fields to be excluded from serialization.
    """

    class Meta:
        model = File
        exclude = ["uploaded"]
