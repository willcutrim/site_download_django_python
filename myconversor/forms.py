from django import forms


class LinkForm(forms.Form):
    link = forms.URLField(label="")


class ImagemForm(forms.Form):
    imagem = forms.ImageField(label="")