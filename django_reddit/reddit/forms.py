from django import forms
from .models import Post, Comment, Profile, Save, Post_Vote, Comment_Vote, Moderator


class PostForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Post
        fields = ('created_at', 'title', 'picture',
                  'content', 'site_url', 'vote_total', 'user')


class CommentForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Comment
        fields = ('created_at', 'content', 'vote_total', 'user', 'post')


class ProfileForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Profile
        fields = ('profile_pic', 'user')


class SaveForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Save
        fields = ('user', 'post', 'created_at')


class Post_VoteForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Post_Vote
        fields = ('user', 'post', 'value')


class Comment_VoteForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Comment_Vote
        fields = ('user', 'comment', 'value')


class ModeratorForm(forms.ModelForm):
    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Moderator
        fields = ('user')
