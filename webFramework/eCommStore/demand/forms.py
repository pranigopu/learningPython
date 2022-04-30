from django.forms import ModelForm, Textarea, TextInput # To define forms based on given model fields.
from django import forms
from .models import * # Importing all the models.

# CUSTOMER DETAIL FORMS
class CustomerEntry(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': TextInput(attrs={'size': 50}),
            'email': TextInput(attrs={'size': 50}),
            'phone': TextInput(attrs={'size': 50}),
            'address': Textarea(attrs={'cols': 41, 'rows': 5, 'style': 'resize:none'})}
        # To include all fields, simply do:
        # fields = '__all__'
        """
        NOTES ON 'Meta':
        For a model form to register the associated model and required fields for the form,
        you must give this information to special variables (model and fields) in a special
        'Meta' subclass defined within the class. This stores the meta data of the form.
        """

# PRODUCT DETAIL FORMS
class ProductEntry(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'size': 50}),
            'description': Textarea(attrs={'cols': 41, 'rows': 5, 'style': 'resize:none'})
        }

# ORDER PLACEMENT FORMS
class OrderPlacement(forms.Form):
    customerId = forms.CharField(label = "Customer ID", max_length = 30)
    customerName = forms.CharField(label = "Customer name", max_length = 30)
    ### TO BE CONTINUED ###
    product = forms.CharField(
        label = "Product",
        widget = forms.Select())

# GENERAL FORMS
class Removal(forms.Form):
    fieldName = forms.CharField(label = "Field name", max_length = 30)
    fieldValue = forms.CharField(label = "Field value", max_length = 30)