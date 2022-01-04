from typing import Coroutine
from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render
from .models import blogpost, Category, Comment

# Create your views here.
def blog(request):
    blog = blogpost.objects.all().order_by("-id")
    allcat = Category.objects.all()
    featured_posts = blogpost.objects.filter(featured_post=True)
    featured_cat = Category.objects.filter(featured=True)
    return render(request, 'blog/blog.html', {"blogs":blog, "allcats":allcat, "featured_posts":featured_posts, "featured_cat":featured_cat})

def blogPost(request, slug):
    blogp = blogpost.objects.get(slug = slug)
    comments = Comment.objects.filter(blog_post__slug = slug).order_by("-id")
    return render(request, 'blog/blogpost.html',{"blogp":blogp, "comments":comments})

def postbycat(request, cat):
    blog = blogpost.objects.filter(category__name=cat)
    allcat = Category.objects.all()
    return render(request, 'blog/blog.html', {"blogs":blog, "allcats":allcat})

def postComment(request):
    if request.method == "POST":
        slugComment = request.POST['slug']
        commentComment = request.POST['comment']

        blogpostComment = blogpost.objects.get(slug = slugComment)
        
        if request.user.is_authenticated:
            comment = Comment(user = request.user.username, blog_post=blogpostComment, comment=commentComment)
            comment.save()
        else:
            comment = Comment(user = "Anonymous user", blog_post=blogpostComment, comment=commentComment)
            comment.save()

        messages.success = "your comment has been added successfully"
        return redirect("/blog/"+slugComment)
    return redirect('/')