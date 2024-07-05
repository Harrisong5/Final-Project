from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Comment
from . forms import CreateUserForm
from django.http import HttpResponse

# Create your views here.
posts = Post.objects.all().order_by('-date')
comments = Comment.objects.all().order_by('-post')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "forum/index.html"
    paginate_by = 6

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redierct('forum/index.html')

    context = {'registerform':form}

    return render (request, 'forum/register.html', context=context)

def my_login(request):

   return HttpResponse("login page")

def dashboard(request):

    return HttpResponse("dashboard")