from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)
