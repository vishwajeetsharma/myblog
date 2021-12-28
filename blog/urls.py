from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name="blog"),
    path('blog/<str:slug>', views.blogPost, name="blogpost"),
]
