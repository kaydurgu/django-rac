from unicodedata import category
from django.urls import path
from . import views
urlpatterns = [
    path('', views.BlogMainView.as_view(), name = 'blog-main'),
    path('details/<pk>',views.BlogDetailsView.as_view(), name = 'post_details'),
    path('write/', views.write_post, name = 'write-blog'),
    path('categories/', views.AllCategoriesView.as_view(), name = 'categories'),
    path('category/<int:pk>',views.CategoryView.as_view() , name = 'blog-by-category'),
    path('<str:username>',views.MyBlogView.as_view() , name = 'my-blogs'),
]