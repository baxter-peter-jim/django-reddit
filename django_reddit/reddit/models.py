from django.db import models


class Post(models.Model):
    created_at = models.CharField(max_length=1000)
    title = models.TextField(max_length=1000)
    picture = models.TextField(max_length=1000)
    content = models.TextField(max_length=1000)
    site_url = models.TextField(max_length=1000)
    vote_total = models.TextField(max_length=1000)
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='users')


def __str__(self):
    return self.created_at


class User(models.Model):
    email = models.CharField(max_length=1000)
    password = models.TextField(max_length=1000)
    username = models.TextField(max_length=1000)


def __str__(self):
    return self.email


class Save(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='saves')
    post = models.ForeignKey(
        Post, on_delete='CASCADE', related_name='saves')
    created_at = models.CharField(max_length=1000)


def __str__(self):
    return self.user


class Comment_Vote(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='comment_votes')
    comment = models.ForeignKey(
        Comment, on_delete='CASCADE', related_name='comment_votes')
    value = models.CharField(max_length=1000)


def __str__(self):
    return self.user


class Moderator(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='moderators')


def __str__(self):
    return self.user
 # Comment Model


class Comment(models.Model):
    created_at = models.CharField(max_length=400)
    content = models.CharField(max_length=400)
    vote_total = models.CharField(max_length=400)
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete='CASCADE', related_name='comments'
    )


def __str__(self):
    return self.content


class Profile(models.Model):
    profile_pic = models.CharField(max_length=400)
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='profile'
    )


def __str__(self):
    return self.profile_pic


class Post_Vote(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='post_votes'
    )
    post = models.ForeignKey(
        Post, on_delete='CASCADE', related_name='post_votes'
    )
    plusOne = '+1'
    minusOne = '-1'
    POST_VOTE_CHOICES = (
        (plusOne, '+1'),
        (minusOne, '-1')
    )
    value = models.CharField(
        max_length=2,
        choices=POST_VOTE_CHOICES
    )


def __str__(self):
    return self.value
