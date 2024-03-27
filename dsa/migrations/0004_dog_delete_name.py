# Generated by Django 4.2.3 on 2024-03-27 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0003_delete_messageform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
