from django import forms


class DemoForm(forms.Form):
    origin = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    destination = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
