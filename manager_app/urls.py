from django.urls import path
from . import views
urlpatterns = [
    path('home/<str:person_slug>', views.show_customized_home_page)
]
