import email
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Person, Task
from .forms import PersonForm, TaskForm
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

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            task = Task(date=clean_data['date'], task_type=clean_data['task_type'],
            person=clean_data['person'], guest=clean_data['guest'])
            task.save()
            return HttpResponseRedirect('/create-task')
    else:
        form = TaskForm()
    return render(request, 'manager_app/create-task.html', {
        "form": form
    })    