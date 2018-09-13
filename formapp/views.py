from django.shortcuts import render
from . import forms

def index(request):
    form_data = forms.FormName1()
    return render(request,"html/form.html",{"formtag":form_data})
