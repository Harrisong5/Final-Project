from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField()

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)