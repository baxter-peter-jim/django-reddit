from django.db import models


class Post(models.Model):
    created_at = models.CharField(max_length=1000)
    title = models.TextField(max_length=1000)
    picture = models.TextField(max_length=1000)
    content = models.TextField(max_length=1000)
    site_url = models.TextField(max_length=1000)
    vote_total = models.TextField(max_length=1000)
    # user = models.ForeignKey(
    #     User, on_delete='CASCADE', related_name='users')


def __str__(self):
    return self.created_at


class Save(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='save')
    post = models.ForeignKey(
        Post, on_delete='CASCADE', related_name='save')
    created_at = models.CharField(max_length=1000)


def __str__(self):
    return self.user


class Comment_Vote(models.Model):
    user = models.ForeignKey(
        User, on_delete='CASCADE', related_name='comment_vote')
    comment = models.ForeignKey(
        Comment, on_delete='CASCADE', related_name='comment_vote')
    value = models.CharField(max_length=1000)


def __str__(self):
    return self.user
