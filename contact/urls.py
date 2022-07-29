from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name = 'contact'),
    path('messages/' ,views.CustomerMessageView.as_view(), name='customer-messages'),
]