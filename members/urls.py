from django.urls import path
from . import views
from .views import LikedBlogView

urlpatterns = [
    path('settings/<str:username>/', views.settings, name = 'settings'),
    path('follow/<str:username>/',views.follow, name = 'follow'),
    path('<str:username>/', views.profile, name = 'profile'),
    path('<str:username>/liked', LikedBlogView.as_view(), name = 'liked'),
]
