from django.db import models

# Create your models here.
class blogpost(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to="blog/featrued_image/")
    main_image = models.ImageField(upload_to="blog/main_image/")
    content = models.TextField()
    date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name+" - "+str(self.date)