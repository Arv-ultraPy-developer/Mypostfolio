from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills'),
    path('project', views.project, name='project'),
    path('signing', views.signing, name='signing'),
    path('myportfolio', views.myportfolio, name='myportfolio'),
    path('contact', views.contact, name='contact'),
    path('submitted', views.submitted, name='submitted'),
]