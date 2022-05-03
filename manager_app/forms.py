from django import forms
from .models import Person, Task
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['slug']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'admin': 'Administrador'
        }        


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'date': 'Data',
            'task_type': 'Tipo de designação',
            'person': 'Participante',
            'guest': 'Ajudante'
        }
        widgets = {
            'date': forms.SelectDateWidget
        }






