from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, authenticate
from .forms import MyUserCreationForm, PostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'basr.html', {'posts': posts})


def post(request, pk):
    posts = get_object_or_404(Post, id=pk)
    return render(request, 'post.html', {'posts': posts})


def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': MyUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()
            login(request, user)  # Вход пользователя
            return redirect('home')
        else:
            return render(request, 'register.html',
                          {'form': MyUserCreationForm(), 'error': 'Passwords do not match'})


def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Вход пользователя
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def create_post(request):
    if request.method == 'GET':
        return render(request, 'create_post.html', {'form': PostForm})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            push = form.save(commit=False)
            push.user = request.user
            push.save()
            return redirect('home')


def edit_post(request, rec_pk):
    posts = get_object_or_404(Post, pk=rec_pk, user=request.user)
    if request.method == 'GET':
        form = PostForm(instance=posts)
        return render(request, 'edit_post.html', {'posts': posts, 'form': form})
    else:
        form = PostForm(request.POST, request.FILES, instance=posts)
        form.save()
        return redirect('home')


def delete_post(request, rec_pk):
    recipes = get_object_or_404(Post, pk=rec_pk, user=request.user)
    if request.method == 'POST':
        recipes.delete()
        return redirect('home')
