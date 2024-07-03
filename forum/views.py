from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

# Create your views here.
posts = Post.objects.all().order_by('-date')
comments = Comment.objects.all().order_by('-post')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "forum/index.html"
    paginate_by = 6

