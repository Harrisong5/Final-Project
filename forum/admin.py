from django.contrib import admin
from .models import Post, Community, JoinComm

# Register your models here.
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(JoinComm)
