from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, authenticate
from .forms import MyUserCreationForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    posts = get_object_or_404(Post, id=pk)
    return render(request, 'post.html', {'posts': posts})


def signup(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': MyUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()
            login(request, user)  # Вход пользователя
            return redirect('index')
        else:
            return render(request, 'login.html',
                          {'form': MyUserCreationForm(), 'error': 'Passwords do not match'})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def login(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': AuthenticationForm()})
    else:
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)  # Вход пользователя
            return redirect('index')
        except AttributeError:
            return render(request, 'signup.html',
                          {'form': AuthenticationForm(), 'error': 'Password is not correct'})