from django.shortcuts import render
from . import forms

def index(request):
    form_data = forms.FormName1()

    if request.method=="POST":
        form_data=forms.FormName1(request.POST)
        if form_data.is_valid():
            print("First_Name  "+form_data.cleaned_data['First_Name'])
            print("Last_Name  "+form_data.cleaned_data['Last_Name'])
            print("Email  "+form_data.cleaned_data['Email'])
            print("Address  "+form_data.cleaned_data['Address'])
    return render(request,"html/form.html",{"formtag":form_data})
