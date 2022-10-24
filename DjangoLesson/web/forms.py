from django import forms

class MyForm(forms.Form):
    surname = forms.CharField(max_length=8)
    name = forms.CharField(max_length=15)
    age = forms.IntegerField()