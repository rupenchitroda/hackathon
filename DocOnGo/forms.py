from django import forms

class DetailForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    str = forms.CharField(max_length=1000)
    