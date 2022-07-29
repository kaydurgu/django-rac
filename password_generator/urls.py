from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'password_generator/home.html') , name = 'password-generator'),
    path('genereted-password', views.genereted_password , name = 'genereted-password')
]