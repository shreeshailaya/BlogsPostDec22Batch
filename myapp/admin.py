from django.contrib import admin
from myapp.models import Blog, Comment

# Register your models here.

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['tags']
    list_display = ['title', 'description', 'tags', 'img']

admin.site.register(Comment)


    