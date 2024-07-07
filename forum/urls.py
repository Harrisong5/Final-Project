from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.PostList.as_view(), name='forum'),
    path('register', views.register, name='register'),
    path('login', views.my_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    
    

]