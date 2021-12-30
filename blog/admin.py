from django.contrib import admin
from .models import Comment, blogpost, Category
# Register your models here.


class blogPostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'slug', 'content']
    list_display = ['name', 'category', 'description', 'slug', 'date']


class commentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog_post', 'date', 'comment']

admin.site.register(blogpost, blogPostAdmin)
admin.site.register(Category)
admin.site.register(Comment, commentAdmin)