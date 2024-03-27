# Generated by Django 4.2.3 on 2024-03-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0008_dog_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='name',
        ),
        migrations.AddField(
            model_name='dog',
            name='text',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
