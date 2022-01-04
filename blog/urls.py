from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name="blog"),
    path('blogs/comment/', views.postComment, name="blogpostComment"),
    path('blog/<str:slug>', views.blogPost, name="blogpost"),
    path('blog/category/<str:cat>', views.postbycat, name="postbycat"),
]
