
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import Register
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, Register
from django.views.generic import ListView
from blog.models import Blog
from .models import Profile

@login_required
def follow(request, username):
    user = get_object_or_404(Profile, user__username = username)
    following_user = request.user.profile
    if user in following_user.followings.all():
        following_user.followings.remove(user)
        user.followers.remove(following_user)
    else:
        following_user.followings.add(user)
        user.followers.add(following_user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            new_user = form.save()
            prof = Profile(user = new_user)
            new_user.save()
            prof.save()
            messages.success(request, 'You have been successfuly registred')
            return redirect('register')
    return render(request, 'members/register.html', {'form' : form})
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request,f'You are now logged in as {username}.')
                return redirect('home')
            else:
                messages.error(request,f' f"Error"')
                return redirect('login')
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'members/login.html', {'form' : form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been successfuly logout')
    return redirect('home')

def profile(request,username):
    profile_of_user = get_object_or_404(Profile, user__username = username)
    is_following = None
    if request.user.is_authenticated:
        is_following = request.user.profile in profile_of_user.followers.all()
    print (is_following)
    return render(request, 'members/profile.html', {'profile_of_user':profile_of_user , 'is_following':is_following})


@login_required
def settings(request,username):

    users = get_object_or_404(User, username=username)
    if request.method == 'POST':

        users.first_name = request.POST['first_name']
        users.last_name = request.POST['last_name']
        profile = users.profile

        profile.bio = request.POST['bio']
        profile.twitter = request.POST['twitter']
        profile.facebook = request.POST['facebook']
        profile.instagram = request.POST['instagram']

        if request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        else:
             profile.profile_pic = users.profile.profile_pic
        profile.save()
        users.save()
        messages.success(request, 'You have successfuly changed ur profile settings')
        return redirect('profile', username=username) 

    if request.user.username == users.username:
        initial_dict = {
            'username':users.username,
            'first_name':users.first_name,
            'last_name':users.last_name,
            'bio':users.profile.bio,
            'twitter':users.profile.twitter,
            'facebook':users.profile.facebook,
            'instagram':users.profile.instagram, 
            'profile_pic':users.profile.profile_pic,
        }
        form = UserForm(initial = initial_dict)
        return render(request, 'members/settings.html', {'form':form})
    return HttpResponse('<h1>404 PAGE not found</h1>')

class LikedBlogView(ListView):
    template_name = 'members/liked.html'
    model = Blog
    context_object_name = 'post'
    



# Settings Not Working