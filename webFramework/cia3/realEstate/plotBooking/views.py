from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse # EXTRA CODE

# Create your views here.
def create_customer(request):
    form = CustomerEntryForm()
    if request.method == "POST":
        form = CustomerEntryForm(request.POST)
        form.save()
        return HttpResponse('Entry successful!') # EXTRA CODE
    return render(request, 'entryForm.html', {'title': 'Customer entry form', 'form': form})