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
