# Generated by Django 3.2.15 on 2023-01-05 13:36

import bottle_defect.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle_defect', '0004_auto_20230105_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload_table',
            name='images',
            field=models.ImageField(blank=True, default='/Images/None/No-img.jpg', max_length=255, upload_to=bottle_defect.models.upload_path),
        ),
    ]