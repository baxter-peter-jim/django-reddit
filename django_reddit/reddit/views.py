from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, User, Save, Comment_Vote, Moderator, Comment, Profile, Post_Vote
from .forms import PostForm, CommentForm, UserForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def post_index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'reddit/post_index.html', context)


def post_show(request, pk):
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'reddit/post_show.html', context)


@login
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_index')
    else:
        form = PostForm()
    return render(request, 'reddit/post_form.html', {'form': form})


@login_required
def comment_new(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('post_index')
    else:
        form = FadForm()
    return render(request, 'reddit/comment_form.html', {'form': form})
