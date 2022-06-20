from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


from .forms import CommentForm
from .models import Blog, Comment


def blog_main(request):
    queryset = Blog.objects.order_by('-id')   
    return render(request, 'blog/blog_main.html', {'posts' : queryset})

def post_details(request, post_id):
    post = get_object_or_404(Blog,id = post_id) 
    if request.method == 'POST':
        request.method = ''
        comment_text = request.POST['comment_text']
        new_com = Comment(blog_id = post, comment_text = comment_text)
        new_com.save()
        return redirect('post_details',post_id = post_id)
    comments = Comment.objects.filter(blog_id = post_id).order_by('-id')
    form = CommentForm()
    return render(request, 'blog/post_details.html',{'post' : post,'form':form, 'comments':comments})
