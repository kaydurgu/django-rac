from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('details/<int:pk>', views.PostDetailView.as_view(), name = 'details-project'),
    path('make-advertisment', views.make_advertisment, name='make-advertisment'),
]