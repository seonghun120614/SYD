# Generated by Django 5.0.6 on 2024-05-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('csv', models.FileField(upload_to='')),
                ('uploaded', models.TimeField(auto_now=True)),
            ],
        ),
    ]
