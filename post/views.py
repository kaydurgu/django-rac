
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Project
from .forms import AdvertismentForm

class HomeView(ListView):
    model = Project
    template_name: str = 'post/main.html'
    context_object_name = 'Projects'
    

@login_required
def make_advertisment(request):
    form = AdvertismentForm()
    if request.method == 'POST':
        form = AdvertismentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Success Added')
            return redirect('home')
    return render(request, 'post/write_post.html', {'form' : form })


class PostDetailView(DetailView):

    model = Project
    template_name: str = 'post/details_proj.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
