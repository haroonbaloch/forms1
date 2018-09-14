from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should be start with Z")

class FormName1(forms.Form):
    First_Name=forms.CharField(max_length=256, validators=[check_for_z])
    Last_Name=forms.CharField(max_length=256)
    Email=forms.EmailField(max_length=256)
    Email2=forms.EmailField(max_length=256)
    Address=forms.CharField()
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['Email']
        vemail=all_clean_data['Email2']

        if email != vemail:
            raise forms.ValidationError("Email dont match")
