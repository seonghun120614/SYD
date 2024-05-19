from django.db import models


class CSVFile(models.Model):
  title = models.CharField(max_length=50)
  csv = models.FileField()
  uploaded = models.TimeField(auto_now=True);
  
  def __str__(self):
    return f"{self.title}"