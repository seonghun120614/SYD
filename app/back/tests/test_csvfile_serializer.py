from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import CSVFile
from api.serializers import CSVFileSerializer

class CSVFileSerializerTest(TestCase):

    def test_csvfile_serialization(self):
        """
        Test serialization of a CSVFile instance.

        This method tests the serialization of a CSVFile instance using CSVFileSerializer.
        It checks if the serialized data contains the expected values.
        """
        # Create a SimpleUploadedFile object representing a CSV file
        csv_file = SimpleUploadedFile(
            "test1.csv", b"a,b\n1,val\n2,seven", content_type="text/csv"
        )

        # Create a CSVFile instance in the database
        csvfile_instance = CSVFile.objects.create(
            title="test1", csv=csv_file
        )

        # Test serialization of the CSVFile instance
        serializer = CSVFileSerializer(csvfile_instance)
        data = serializer.data

        self.assertEqual(data['title'], "test1")
        self.assertIn("test1.csv", data['csv'])
        self.assertNotIn('uploaded', data)

    def test_csvfile_deserialization(self):
        """
        Test deserialization and creation of a new CSVFile instance.

        This method tests the deserialization of data and creation of a new CSVFile instance
        using CSVFileSerializer. It checks if the deserialized data is valid and if a new
        CSVFile instance is created with the provided data.
        """
        # Test deserialization and creation of a new CSVFile instance
        data = {
            'title': "new_test",
            'csv': SimpleUploadedFile("new_test.csv", b"te,st\n1,2", content_type="text/csv")
        }

        serializer = CSVFileSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        csvfile_instance = serializer.save()

        self.assertEqual(csvfile_instance.title, "new_test")
        self.assertTrue(csvfile_instance.csv)
        self.assertIn("new_test.csv", csvfile_instance.csv.name)
