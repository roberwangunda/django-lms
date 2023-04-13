from django import forms
from django.db import transaction

from .models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
