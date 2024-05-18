from django.db import models


class TestModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=10, blank=True, default='')  
  class Meta:
    ordering = ['created']
    