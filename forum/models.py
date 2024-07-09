from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

# Helps user find posts on chosen topics
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

# Joins a user to be able to post in a specific community
class JoinComm(models.Model):
    JoinCommUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_joined_comms")
    JoinComm = models.ManyToManyField(Community, related_name="forum_comms")
    Joined = models.CharField(max_length=100, null=True, blank=True, default='FALSE')

    def __str__(self):
        return self.JoinCommUser.username

# Model for a post
class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="post_community")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    imgLink = models.CharField(max_length=1500, null=True, blank=True)
    youtubeLink = models.CharField(max_length=1500, null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    date = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField(User, related_name="votes")
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            import re

            def slugify(s):
                s = s.lower().strip()
                s = re.sub(r'[^\w\s-]', '', s)
                s = re.sub(r'[\s_-]+', '-', s)
                s = re.sub(r'^-+|-+$', '', s)
                return s
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# Model for comments on a specific post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    commentBody = models.TextField(max_length=10000, null=True, blank=True)
    commentVote = models.ManyToManyField(User, related_name="comment_vote")
    commentDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.commentBody
