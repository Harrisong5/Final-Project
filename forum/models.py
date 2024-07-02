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

class Sub(models.Model):
    sub_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)