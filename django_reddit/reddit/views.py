from django.shortcuts import render, redirect
from .models import Post, User, Save, Comment_Vote, Moderator, Comment, Profile, Post_Vote
from .forms import PostForm, CommentForm

# Create your views here.

def post_index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'reddit/post_index.html', context)

def post_show(request, pk):
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'reddit/post_show.html', context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_index')
    else:
        form = PostForm()
    return render(request, 'reddit/post_form.html', {'form': form})