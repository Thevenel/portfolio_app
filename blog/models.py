from distutils.command.upload import upload
from django.db import models
from datetime import datetime

from django.forms import ImageField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    pub_date = datetime.now()
    content = models.TextField()
    blog_img = models.ImageField(upload_to='blog-images/')

    def __str__(self):
        return self.title


    def summary(self):
        return self.content[:200]

    def format_date(self):
        return self.pub_date.strftime('%B %e, %Y')