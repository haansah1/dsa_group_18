from django.db import models
from django import forms

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.name

class MessageForm(models.Model):
    message = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

# Define a form class that inherits from ModelForm
class MessageFormForm(forms.ModelForm):
    class Meta:
        model = MessageForm  # Use the MessageForm model
        fields = ['message', 'file']  # Include the desired fields in the form
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Specify widget for the message field
        }