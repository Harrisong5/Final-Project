from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Post

# User register


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User log in 


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# User changing password


class PasswordForm(PasswordChangeForm):
   
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    class Meta:
        model = User
        fields = [ 'old_password', 'new_password1', 'new_password2']    

# User create a new post


class CreatePostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        exclude = ('date', 'votes', 'slug', 'status' )
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'})
        }

# User edit one of their existing posts


class EditPostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        exclude = ('date', 'votes', 'slug', )
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'status': forms.TextInput(attrs={'value': 0, 'id':'status', 'type':'hidden'}),
    
        }

# User delete one of their existing posts


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postID']