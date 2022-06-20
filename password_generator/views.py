from django.http import HttpResponse
from django.shortcuts import render
import string
import random

def home(request):
    return render(request, 'password_generator/home.html')

def genereted_password(request):
    
    char = list(string.ascii_lowercase)
    special = '?,.!@#$%&'
    if request.GET.get('uppercase'):
        char.extend(list(string.ascii_uppercase))
    if request.GET.get('digits'):
        char.extend(list(list(string.digits)))
    if request.GET.get('special'):
        char.extend(list(special))

    length = int(request.GET.get('length', 10))
    length = min(length, 12)
    
    thepassword = ''
    statment = False
    
    if len(request.GET):
        statment = True
    for i in range(length):
       thepassword += random.choice(char)
    
    return render(request, 'password_generator/password.html',{'password' : thepassword, 'statment':statment})
