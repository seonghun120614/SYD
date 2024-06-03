from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile


class CSVFile(models.Model):
    """
    Model representing a CSV file.

    This model is used to store information about CSV files uploaded to the system.
    It interacts with the database to store, retrieve, and manage CSV file data.
    Each CSV file has a title, which represents the name of the file, and the actual
    CSV file is stored using the 'csv' field. The 'uploaded' field stores the time
    when the file was uploaded to the system.

    Attributes:
        title (CharField): The title of the CSV file.
        csv (FileField): The CSV file itself, stored as a file.
        uploaded (TimeField): The time when the file was uploaded to the system.
    """

    title = models.CharField(max_length=50)
    csv = models.FileField()
    uploaded = models.TimeField(auto_now=True)

    def __str__(self):
        """
        Return string representation of the CSV file.

        Returns:
            str: Title of the CSV file.
        """
        return f"{self.title}"
