from django.contrib import admin
from .models import blogpost
# Register your models here.


class blogPostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'slug', 'content']
    list_display = ['name', 'description', 'slug', 'date']

admin.site.register(blogpost, blogPostAdmin)