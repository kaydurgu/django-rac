from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .escript import Mail
from django.contrib import messages
# Create your views here.
def contact(request):
    if len(request.GET):
        name = request.GET['name']
        email = request.GET['email']
        message = request.GET['message']

        mail = Mail()
        try:
            mail.send(name, email, message)
        except:
            return HttpResponse('Your message has not been sent try again later')
        return redirect('contact')
    return render(request, 'contact/contact.html')