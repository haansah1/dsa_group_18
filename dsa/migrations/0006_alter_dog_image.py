# Generated by Django 4.2.3 on 2024-03-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0005_remove_dog_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
