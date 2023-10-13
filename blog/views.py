
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from . models import Blog , Tag , Category

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    
    context = {
        "blogs":blogs,
    }

    return render(request,"blog/blog_list.html",context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created_at")[:5]
    categories = Category.objects.all()
    context = {
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
    }
    return render(request,"blog/blog_detail.html",context)