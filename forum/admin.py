from django.contrib import admin
from .models import Community, JoinComm, Post

# Register your models here.
admin.site.register(Community)
admin.site.register(JoinComm)
admin.site.register(Post)