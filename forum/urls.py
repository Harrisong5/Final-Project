from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='forum'),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('dashboard', views.dashboard, name='dashboard'),
]