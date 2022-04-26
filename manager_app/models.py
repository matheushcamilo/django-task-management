from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(blank=True, unique=True)
    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name


class Task(models.Model):
    
    class TaskType(models.TextChoices):
        PRIMEIRA_VISITA = 'PV', 'Primeira Visita'
        SEGUNDA_VISITA = 'SV', 'Segunda Visita'
        DISCURSO = 'D', 'Discurso'
        DISURSO_PUBLICO = 'DP', 'Discurso Público'
    

    date = models.DateField(null=False, blank=False)
    task_type = models.CharField(max_length=2, null=False, blank=False, choices=TaskType.choices)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')

    def __str__(self):
        return f"{self.task_type} on {self.date}"
