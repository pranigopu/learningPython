from django import forms
from .models import *
class CustomerEntryForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'