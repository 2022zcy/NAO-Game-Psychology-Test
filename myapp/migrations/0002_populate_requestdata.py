# Generated by Django 5.1 on 2024-09-05 14:23

from django.db import migrations

def create_initial_data(apps, schema_editor):
    RequestData = apps.get_model('myapp', 'RequestData')
    RequestData.objects.create(request_type=1, message='1')

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(create_initial_data)
    ]
