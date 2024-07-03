from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment

# Create your views here.
posts = Post.objects.all().order_by('-date')
comments = Comment.objects.all()

def my_forum(request):
    return HttpResponse(comments)

    