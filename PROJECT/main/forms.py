from django import forms
import account.forms
from django.forms import ModelForm

from .models import *


class ClockForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new alarm...'}))
    settedtime = forms.DateTimeField()
    text = forms.CharField()

    class Meta:
        model = Clock
        fields = ['title', 'settedtime', 'text']


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)


