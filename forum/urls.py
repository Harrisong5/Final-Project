from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.PostList.as_view(), name='forum'),
    path('register', views.register, name='register'),
    path('login', views.my_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('change_password', views.PasswordChange.as_view(template_name = "forum/change_password.html"), name="change_password"),
    path('password_success', views.password_success, name="password_success"),
    path('create_post', views.CreatePost.as_view(), name="create_post"),
    
    
]