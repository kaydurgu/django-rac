from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name = 'password-generator'),
    path('genereted-password', views.genereted_password , name = 'genereted-password')
]