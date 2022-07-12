import email
from email import message
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render( request, 'home.html')

def about(request):
    return render( request, 'aboutme.html')    

def skills(request):
    return render( request, 'skills.html')      

def project(request):
    return render( request, 'project.html')    

def signing(request):
    return render( request, 'si&su.html')    

def myportfolio(request):
    return render( request, 'myportfolio.html')   

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages = request.POST.get('description')

        data ={
            'name':name,
            'email': email,
            'messages':messages
        }
        messages = '''
        New message: {}

        From: {}

        Name or Company: {}
        '''.format(data['messages'], data['email'],data['name'])
        send_mail(data['name'], messages,'',['aravnaive2020@gmail.com'])
    return render( request, 'contact.html',{})  

def submitted(request):
    return render( request, 'submitted.html')            