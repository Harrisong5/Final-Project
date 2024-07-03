from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

# Create your views here.
posts = Post.objects.all().order_by('-date')
comments = Comment.objects.all().order_by('-post')
class PostList(generic.ListView):
    model = Post
    