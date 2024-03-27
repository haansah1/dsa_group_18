from django.db import models

# Create your models here.
class Textmod(models.Model):
    text = models.FileField(blank = True, upload_to = 'uploads/')

