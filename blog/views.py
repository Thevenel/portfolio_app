from django.shortcuts import render

import blog
from . models import BlogPost
# Create your views here.
def allblogs(request):
    blogs = BlogPost.objects
    return render(request, 'blog/blog.html', {'blogs' : blogs})

def detail(request):
    return render(request, '/blog/blog_detail.html')