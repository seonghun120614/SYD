from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from api.models import CSVFile


class CSVFileModelTest(TestCase):
    def setUp(self):
        # Create a SimpleUploadedFile object representing a CSV file
        self.csv_file = SimpleUploadedFile(
            "test2.csv", b"Age,Name\n19,Park\n23,Sue", content_type="text/csv"
        )
        # Create a CSVFile object in the database
        self.csvfile_instance = CSVFile.objects.create(
            title="test2", csv=self.csv_file
        )

    def test_csvfile_creation(self):
        """
        Test creating a CSVFile object.

        This method tests the creation of a CSVFile object in the database
        with the provided CSV file.
        """
        # Check if the created instance is an instance of CSVFile model
        self.assertIsInstance(self.csvfile_instance, CSVFile)
        # Check if the title of the CSVFile instance matches the expected value
        self.assertEqual(self.csvfile_instance.title, "test2")
        # Check if the 'csv' field of the CSVFile instance is not empty
        self.assertTrue(self.csvfile_instance.csv)
        # Check if the name of the uploaded CSV file matches the expected value
        self.assertIn("test2.csv", self.csvfile_instance.csv.name)
