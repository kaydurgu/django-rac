
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Book
from django.core.paginator import Paginator,PageNotAnInteger ,EmptyPage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class BookListView(ListView):
    model = Book
    template_name = 'crud/list.html'
    context_object_name = 'books'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context

@method_decorator(login_required, name='dispatch')
class BookCreatView(CreateView):
    model = Book
    template_name = 'crud/create.html'
    fields = ('name', 'isbn_number', )
    success_url = reverse_lazy('book-list')

@method_decorator(login_required, name='dispatch')
class BookDetailsView(DetailView):
    model = Book
    template_name = 'crud/details.html'
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'crud/update.html'
    context_object_name = 'book'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('details', kwargs = {'pk' : self.kwargs['pk']})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('book-list')
    