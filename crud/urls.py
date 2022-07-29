
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(),
        name='book-list'),
    path('create_book', views.BookCreatView.as_view(), 
        name = 'create-book'),
    path('book/<int:pk>', views.BookDetailsView.as_view(),
        name = 'details'),
    path('update/<int:pk>' ,views.BookUpdateView.as_view(),
        name = 'update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(),
        name = 'delete'),
]