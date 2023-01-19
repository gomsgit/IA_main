# Generated by Django 3.2.15 on 2023-01-06 07:53

import bottle_defect.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle_defect', '0005_alter_file_upload_table_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded_file_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='/Images/None/No-img.jpg', max_length=255, upload_to=bottle_defect.models.upload_path)),
                ('name', models.CharField(max_length=100)),
                ('batch_name', models.CharField(max_length=100)),
                ('upload_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='File_upload_table',
        ),
    ]