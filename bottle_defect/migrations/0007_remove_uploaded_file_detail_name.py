# Generated by Django 3.2.15 on 2023-01-06 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bottle_defect', '0006_auto_20230106_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_file_detail',
            name='name',
        ),
    ]
