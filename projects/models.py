from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
