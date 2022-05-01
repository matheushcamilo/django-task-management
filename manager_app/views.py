import email
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .forms import PersonForm
# Create your views here.

def show_customized_home_page(request, person_slug):
    try:
        person = Person.objects.get(slug=person_slug)
        if(person.admin is False):
            return render(request, 'manager_app/home.html', {
                "person": person,
                "tasks": person.tasks.all(),
                "participations": person.participations.all()
            })
        else:
            people = Person.objects.all()
            return render(request, 'manager_app/all-people.html', {
                "people": people
            })
    except:
        raise Http404()    

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            person = Person(name=clean_data['name'], email=clean_data['email'], admin=clean_data['admin'])
            person.save()
            return HttpResponseRedirect('/create-person')      
    else:
        form = PersonForm()
    return render(request, 'manager_app/create-person.html', {
        'form': form
    })                