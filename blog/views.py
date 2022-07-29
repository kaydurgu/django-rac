
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommentForm, BlogForm
from .models import Blog, Comment, Category



class BlogMainView(ListView):
    template_name = 'blog/blog_main.html'
    model = Blog
    queryset = Blog.objects.all().order_by('-pk')
    context_object_name = 'posts'
    def get_queryset(self):
        return super().get_queryset()
    def post(self, request):
        state = list(request.POST)[-1]
        blog = Blog.objects.get(pk = request.POST[state])
        if state == 'like':
            if not request.user in blog.likes.all():
                blog.likes.add(request.user)
                if request.user in blog.dislikes.all():
                    blog.dislikes.remove(request.user)
            else:
                blog.likes.remove(request.user)
        elif state == 'dislike':
            if not request.user in blog.dislikes.all():
                blog.dislikes.add(request.user)
                if request.user in blog.likes.all():
                    blog.likes.remove(request.user)
            else:
                blog.dislikes.remove(request.user)
        return redirect('blog-main')


class BlogDetailsView(DetailView):
    template_name: str = 'blog/post_details.html'
    model = Blog
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(blog_id = self.kwargs['pk']).order_by('-pk')
        return context
    def post(self, request ,*args , **kwargs):
        if request.POST.get('comment'):
            if request.user.is_authenticated:
                comment_text = request.POST['comment_text']
                new_com = Comment(user = request.user, blog_id = self.get_object(), comment_text = comment_text)
                new_com.save()
            else:
                return redirect('login')
        else:
            blog = self.get_object()
            state =  list(request.POST)[-1]
            if state == 'like':
                if not request.user in blog.likes.all():
                    blog.likes.add(request.user)
                    if request.user in blog.dislikes.all():
                        blog.dislikes.remove(request.user)
                else:
                    blog.likes.remove(request.user)
            elif state == 'dislike':
                if not request.user in blog.dislikes.all():
                    blog.dislikes.add(request.user)
                    if request.user in blog.likes.all():
                        blog.likes.remove(request.user)
                else:
                    blog.dislikes.remove(request.user)
        return redirect('post_details', pk = self.kwargs['pk'])


@login_required(login_url='/login/')
def write_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.author = request.user
            todo_list.save()
            form.save_m2m()
            messages.success(request, 'You have successfuly posted')
            return redirect('write-blog')
    form = BlogForm()
    return render(request, 'blog/write_blog.html', {'form':form})

class MyBlogView(ListView):
    template_name: str = 'blog/my_blogs.html'
    context_object_name = 'posts'
    model = User
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        return user.blog_set.all()
    def post(self, request, *args , **kwargs):
        blog = Blog.objects.get(pk = request.POST[list(request.POST)[-1]])
        state =  list(request.POST)[-1]
        if state == 'like':
            if not request.user in blog.likes.all():
                blog.likes.add(request.user)
                if request.user in blog.dislikes.all():
                    blog.dislikes.remove(request.user)
            else:
                blog.likes.remove(request.user)
        elif state == 'dislike':
            if not request.user in blog.dislikes.all():
                blog.dislikes.add(request.user)
                if request.user in blog.likes.all():
                    blog.likes.remove(request.user)
            else:
                blog.dislikes.remove(request.user)
        return redirect('my-blogs', username = self.kwargs['username'])
class CategoryView(ListView):

    template_name = 'blog/category.html'
    context_object_name = 'posts'
    model = Category

    def get_queryset(self):
        qr = get_object_or_404(self.model,pk = self.kwargs['pk'])
        return qr.blog_set.all()

    def post(self, request, *args, **kwargs):
        blog = Blog.objects.get(pk = request.POST[list(request.POST)[-1]])
        state =  list(request.POST)[-1]
        if state == 'like':
            if not request.user in blog.likes.all():
                blog.likes.add(request.user)
                if request.user in blog.dislikes.all():
                    blog.dislikes.remove(request.user)
            else:
                blog.likes.remove(request.user)
        elif state == 'dislike':
            if not request.user in blog.dislikes.all():
                blog.dislikes.add(request.user)
                if request.user in blog.likes.all():
                    blog.likes.remove(request.user)
            else:
                blog.dislikes.remove(request.user)
        return redirect('blog-by-category', pk = self.kwargs['pk'])
        
class AllCategoriesView(CreateView):
    model = Category
    fields = ['category']
    template_name = 'blog/categories.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Category.objects.all()
        return context
    def get_success_url(self):
        return reverse('categories', kwargs={})
