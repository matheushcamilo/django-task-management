from datetime import datetime
from django import forms
from .models import Person, Task
class PersonForm(forms.Form):
    name = forms.CharField(max_length=25, label='Nome')
    email = forms.EmailField(label='E-mail')
    admin = forms.BooleanField(required=False, label='Administrador')


TASK_TYPE_CHOICES = (('PV', 'Primeira Visita'),
        ('SV', 'Segunda Visita'),
        ('D', 'Discurso'),
        ('DP', 'Discurso Público'))
class TaskForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.today)
    task_type = forms.CharField(max_length=20, widget=forms.Select(choices=TASK_TYPE_CHOICES))
    person = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
    guest = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)