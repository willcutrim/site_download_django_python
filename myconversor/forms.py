from django import forms


class LinkForm(forms.Form):
    link = forms.CharField(max_length=155)