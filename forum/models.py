from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Community(models.Model):
    commUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_communities")
    commTitle = models.CharField(max_length=200)
    commURL = models.CharField(max_length=500, null=True, blank=True)
    commImg = models.ImageField(max_length=2000, null=True, blank=True)
    commImglink = models.CharField(max_length=500, null=True, blank=True)
    commDesc = models.TextField(max_length=1000, null=True, blank=True)
    commDate = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.commTitle



class Sub(models.Model):
    sub_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)