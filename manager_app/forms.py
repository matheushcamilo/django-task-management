from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=25, label='Nome')
    email = forms.EmailField(label='E-mail')
    admin = forms.BooleanField(required=False, label='Administrador')
