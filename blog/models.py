from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    featured = models.BooleanField()

    def __str__(self):
        return self.name

class blogpost(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_post = models.BooleanField(default=False)

    featured_image = models.ImageField(upload_to="blog/featrued_image/")
    main_image = models.ImageField(upload_to="blog/main_image/")
    content = models.TextField()
    date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name+" - "+str(self.date)

class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=155)
    blog_post = models.ForeignKey(blogpost, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)+" - "+self.comment

class Image(models.Model):
    image = models.ImageField(upload_to="blog/blog-images/")