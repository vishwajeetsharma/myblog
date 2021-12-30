from typing import Coroutine
from django.shortcuts import render
from .models import blogpost, Category, Comment

# Create your views here.
def blog(request):
    blog = blogpost.objects.all().order_by("-id")
    allcat = Category.objects.all()
    return render(request, 'blog/blog.html', {"blogs":blog, "allcats":allcat})

def blogPost(request, slug):
    blogp = blogpost.objects.get(slug = slug)
    comments = Comment.objects.filter(blog_post__slug = slug)
    return render(request, 'blog/blogpost.html',{"blogp":blogp, "comments":comments})

def postbycat(request, cat):
    blog = blogpost.objects.filter(category__name=cat)
    allcat = Category.objects.all()
    return render(request, 'blog/blog.html', {"blogs":blog, "allcats":allcat})