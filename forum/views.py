from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Post, Comment
from . forms import CreateUserForm, LoginForm, PasswordForm, CreatePostForm, EditPostForm, DeleteForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.http import HttpResponse

# Create your views here.
posts = Post.objects.all().order_by('-date')
comments = Comment.objects.all().order_by('-post')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name = "forum/index.html"
    paginate_by = 6

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my_login')
    else:
        form = CreateUserForm()
    return render(request, 'forum/register.html', {'registerform': form})

    context = {'registerform':form}

    return render (request, 'forum/register.html', context=context)

def post_detail(request, pk):
    
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'forum/post_detail.html', {'post': post})

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

                return redirect('dashboard')
            else:
                # Invalid username or password.
                pass
        else:
            # Form is invalid.
            pass          
    else:
        form = LoginForm()
    return render(request, 'forum/my_login.html', {'loginform': form})

    context = {'loginform':form}

    return render (request, 'forum/my_login.html', context=context)

def logout(request):

    auth.logout(request)

    return redirect('forum')

@login_required(login_url="login")
def dashboard(request):

    current_user = request.user
    email = request.user.email
    password = request.user.password
    posts = Post.objects.filter(author=current_user).order_by('-date')
    drafts = Post.objects.filter(author=current_user).filter(status=0).order_by('-date')

    context = {
        'current_user': current_user,
        'posts': posts,
        'drafts': drafts,
        'email': email,
        'password': password,
    }

    return render(request, 'forum/dashboard.html', context)

class PasswordChange(PasswordChangeView):
    form = PasswordForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'forum/password_change_success.html')


class CreatePost(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    form_class = CreatePostForm
    template_name = "forum/create_post.html"
    success_url = "/dashboard"

class EditPost(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    model = Post
    form_class = EditPostForm
    template_name = "forum/edit_post.html"
    #fields = ['community', 'title', 'content', 'imgLink', 'youtubeLink' ]
    success_url = "/dashboard"



class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = DeleteForm
    template_name = 'forum/delete_post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

