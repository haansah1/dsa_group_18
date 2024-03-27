from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    class Meta:
        model = Textmod
        fields = ('text',)
        labels = {
            'text': '',
        }
