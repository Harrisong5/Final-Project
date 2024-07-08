from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Post

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class PasswordForm(PasswordChangeForm):
   
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    class Meta:
        model = User
        fields = [ 'old_password', 'new_password1', 'new_password2']    

class CreatePostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        exclude = ('date', 'votes', 'slug', 'status' )
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'})
        }