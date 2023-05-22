from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'password1': '', 'password2': '', 'username': ''}


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
