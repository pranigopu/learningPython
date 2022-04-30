from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import * # Importing all forms (to render them based on the request).
import pandas as pd
import json
import re

# Create your views here.
#====================================
# GENERAL ITEM REMOVAL FUNCTION
# NOTE: 'request' is an HttpRequest object, and 'model' is Django model object.
# +NOTE: 'pk' is the name of the primary key of the model.
def removal(request, model, title):
    fieldName, fieldValue = "", ""
    form = Removal()
    if request.method == "POST":
        # Accessing the field name (using which we must search the record to remove)
        fieldName = request.POST.get('fieldName')
        # Accessing the field's given value (on whose basis we must search the record to remove)
        fieldValue = request.POST.get('fieldValue')
        # Delete all items...
        if fieldValue == "all":
            model.objects.all().delete()
            return HttpResponse("Deleted all items")
        # Delete particular item...
        else:
            try:
                model.objects.get(**{fieldName: fieldValue}).delete()
                """
                NOTE ON THE ABOVE KEYWORD ARGUMENT UNPACKING
                ___
                Generally, we would get values from the database using
                YourModel.objects.get(fieldName = fieldValue)
                where fieldName is not a string but a keyword argument.

                However, if we have the field name as a string,
                and want to access a record with a particular value in the particular field,
                we cannot give the field name as a keyword argument name, since it is a string.
                To solve this issue, we unpack the dictionary {fieldName: fieldValue} into
                keywork argument name and argument value respectively, using the prefixed symbols '**',
                which denote keywork arguments.
                """
                return HttpResponse("Deleted record with " + fieldName + " = " + fieldValue)
            except:
                return HttpResponse("Record with " + fieldName + " = " + fieldValue + " does not exist")
    return render(request, "removalForm.html", {'title': title, 'form': form})
#====================================
# CUSTOMER ENTRY FORM SUBMISSION
# Function used later to validate form submission.
# 'obj' here is the dictionary-like object 'request.POST' (see explanation at the bottom).
def validateCustomerEntry(obj):
    if re.match(r"^[^0]\d{9,9}", obj.get('phone')) == None: return False
    if re.match(r"[\w_]+(\.[\w_]+)?\@(gmail|hotmail|outlook)\.com", obj.get('email')) == None: return False
    return True

# NOTE: request here is an HttpRequest object, not a string.
def customer_entry(request):
    # print(request.method) # For demo purposes
    if request.method == "POST":
        form = CustomerEntry(request.POST)
        if validateCustomerEntry(request.POST): form.save()
        else: return HttpResponse("Invalid inputs!")
    else:
        form = CustomerEntry()
    # Saves the inputs to the table corresponding to the model
    # (according to the model structure (which is internalised in the model form class))
    title = "New customer entry"
    return render(request, "entryForm.html", {'title': title, 'form': form})

def customer_removal(request):
    return removal(request, Customer, "Customer removal")
#====================================
# PRODUCT ENTRY FORM SUBMISSION
def product_entry(request):
    # print(request.method) # For demo purposes
    if request.method == "POST":
        form = ProductEntry(request.POST)
        form.save()
    else:
        form = ProductEntry()
    title = "New product entry"
    return render(request, "entryForm.html", {'title': title, 'form': form})
#------------------------------------
# PRODUCT REMOVAL
def product_removal(request):
    return removal(request, Product, "Product removal")
#====================================
# NOTES
"""
EXPLANATION OF REQUEST METHOD, FORM ENTRY AND FORM SAVING
___
There are four actions that determine the action to be taken using any input data:
GET, POST, PUT and DELETE
___
POST is present as an attribute in a Python HttpRequest object.
It is a dictionary-like object that contains all the information entered in a form.
___
The request method (denoted as request.method) is another attribute of the request object.
It is a string that mentions the action of the request.
By default, the request method is GET.
Pressing the submit button triggers another request with the same URL that has the POST method.
___
The class 'ProductEntry' is a subclass of 'ModelForm'.
By passing request.POST in its constructor, you pass all the data inputted into the form.
In doing so, you create an object equivalent to a table record.
(Here, we assigned 'form' to this object, meaning 'form' is the identifier of this object)
The 'save' method available for model forms saves the object's data into the database in the appropriate manner.
--x--
Note that if the request method is POST, this means the form has already been rendered in a previous GET request.
Hence, we can save that information before the return statement that renders the form.
"""

def product_data(request):
    # Getting the list of all fields in the model.
    myColumns = [f.name for f in Product._meta.get_fields()]
    # Creating a dataframe (using data from only certain fields)
    df = pd.DataFrame(Product.objects.all().values(*myColumns)[1:])
    # We exclude the 0th attribute, since that attribute is an automatically created serial order field
    # that is not important to us at all.
    #------------
    # Parsing the DataFrame in json format.
    jsonRecords = df.reset_index().to_json(orient ='records')
    data = json.loads(jsonRecords)
    
    return render(request, 'productDetailsTable.html', {'data': data})