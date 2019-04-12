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
