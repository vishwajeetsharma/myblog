from django.shortcuts import render
from .models import blogpost

# Create your views here.
def blog(request):
    blog = blogpost.objects.all().order_by("-id")
    return render(request, 'blog/blog.html', {"blogs":blog})

def blogPost(request, slug):
    blogp = blogpost.objects.get(slug = slug)
    return render(request, 'blog/blogpost.html',{"blogp":blogp})

def postbycat(request, cat):
    blog = blogpost.objects.filter(category__name=cat)
    return render(request, 'blog/blog.html', {"blogs":blog})