from django.db import models


class File(models.Model):
    """
    Model representing a file.

    Attributes:
        title (CharField): The title of the file.
        csv (FileField): The CSV file itself, stored as a file.
        uploaded (TimeField): The time when the file was uploaded to the system.
    """

    title = models.CharField(max_length=50)
    file = models.FileField()
    uploaded = models.TimeField(auto_now=True)

    def __str__(self):
        """
        Return string representation of the file.

        Returns:
            str: Title of the file.
        """
        return f"{self.title}"
