from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'created_date', 'published_date', 'image']

admin.site.register(Post, PostAdmin)