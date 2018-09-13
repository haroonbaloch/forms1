from django import forms

class FormName1(forms.Form):
    First_Name=forms.CharField(max_length=256)
    Last_Name=forms.CharField(max_length=256)
    Email=forms.EmailField(max_length=256)
    Address=forms.CharField()
