from django import forms

class Emailform(forms.Form):
    From = forms.CharField(required=True)
    To = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)