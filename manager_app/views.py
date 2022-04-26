from django.http import Http404
from django.shortcuts import render
from .models import Person
# Create your views here.


def show_customized_home_page(request, person_slug):
    try:
        person = Person.objects.get(slug=person_slug)
        if(person.admin is False):
            return render(request, 'manager_app/home.html', {
                "person": person,
                "tasks": person.tasks.all()
            })
        else:
            people = Person.objects.all()
            return render(request, 'manager_app/all-people.html', {
                "people": people
            })
    except:
        raise Http404()    