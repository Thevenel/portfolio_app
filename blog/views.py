from django.shortcuts import render, get_object_or_404

from . models import BlogPost
# Create your views here.
def allblogs(request):
    blogs = BlogPost.objects
    return render(request, 'blog/blog.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})