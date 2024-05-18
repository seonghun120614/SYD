from django.db import models


class TestModel(models.Model):
  name = models.CharField(max_length=10)
  created = models.DateTimeField(auto_now_add=True)