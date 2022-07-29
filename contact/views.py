from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .escript import Mail
from django.contrib import messages
from .models import CustomerMessage
from django.views.generic import ListView, TemplateView
from django.contrib.admin.views.decorators import staff_member_required


class ContactView(TemplateView):
    template_name = 'contact/contact.html'
    def get(self, request) -> HttpResponse:
        name = request.GET['name']
        email = request.GET['email']
        message = request.GET['message']
        form = CustomerMessage(name = name, email = email, message = message)
        form.save()
        messages.success(request, 'Your message has been Succesfuly sent')
        return redirect('contact')

def contact(request):
    if len(request.GET):
        name = request.GET['name']
        email = request.GET['email']
        message = request.GET['message']
        '''
        mail = Mail()
        try:
            mail.send(name, email, message)
        except:
            return HttpResponse('Your message has not been sent try again later')
        '''
        form = CustomerMessage(name = name, email = email, message = message)
        form.save()
        messages.success(request, 'Your message has been Succesfuly sent')
        return redirect('contact')
    return render(request, 'contact/contact.html')

class CustomerMessageView(ListView):
    model = CustomerMessage
    context_object_name = 'customer_messages'
    template_name: str = 'contact/customer_messages.html'

