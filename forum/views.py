from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Comment
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
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

            return redirect('my_login')

    context = {'registerform':form}

    return render (request, 'forum/register.html', context=context)

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform':form}

    return render (request, 'forum/my_login.html', context=context)

def logout(request):

    auth.logout(request)

    return redirect('forum')

def dashboard(request):

    return render (request, 'forum/dashboard.html')