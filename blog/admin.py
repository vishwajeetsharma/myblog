from django.contrib import admin
from .models import blogpost, Category
# Register your models here.


class blogPostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'slug', 'content']
    list_display = ['name', 'category', 'description', 'slug', 'date']

admin.site.register(blogpost, blogPostAdmin)
admin.site.register(Category)