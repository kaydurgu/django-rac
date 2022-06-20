from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_main, name = 'blog-main'),
    path('details/<int:post_id>',views.post_details, name = 'post_details')
]