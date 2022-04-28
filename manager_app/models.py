from tkinter.messagebox import NO
from django.db import models
from django.utils.text import slugify
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(blank=True, unique=True)
    admin = models.BooleanField(blank=True, default=False)
    slug = models.SlugField(blank=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
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
    guest = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='participations')
    
    def __str__(self):
        return f"{self.task_type} on {self.date}"

    def save(self, *args, **kwargs):
        if(self.check_for_equal_names() or self.is_one_person_task()):
            self.guest = None
        super().save(*args, **kwargs)    

    def check_for_equal_names(self):
        return self.person == self.guest

    def is_one_person_task(self):
        return self.task_type in ('D', 'DP')    