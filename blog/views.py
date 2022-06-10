from django.shortcuts import render
from . models import BlogPost
# Create your views here.
def Blogpost(request):
    blogs = BlogPost.objects
    return render(request, 'blog/blog.html', {'blogs' : blogs})
