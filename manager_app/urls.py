from django.urls import path
from . import views
urlpatterns = [
    path('home/<str:person_slug>', views.show_customized_home_page, name='show-person'),
    path('create-person', views.create_person, name='create-person'),
    path('create-task', views.create_task, name='create-task')
]
