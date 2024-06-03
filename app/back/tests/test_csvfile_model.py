from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from api.models import CSVFile


class CSVFileModelTest(TestCase):
  def setUp(self):
    self.csv_file = SimpleUploadedFile(
      "test2.csv", b"Age,Name\n19,Park\n23,Sue", content_type="text/csv"
    )
    self.csvfile_instance = CSVFile.objects.create(
      title="test2", csv=self.csv_file
    )

  def test_csvfile_creation(self):
    self.assertIsInstance(self.csvfile_instance, CSVFile)
    self.assertEqual(self.csvfile_instance.title, "test2")
    self.assertTrue(self.csvfile_instance.csv)
    self.assertIn("test2.csv", self.csvfile_instance.csv.name)