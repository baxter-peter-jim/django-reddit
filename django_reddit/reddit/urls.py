from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('posts/<int:pk>/', views.post_show, name='post_show'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk/comments/new', views.comment_new, name='comment_new'),
]