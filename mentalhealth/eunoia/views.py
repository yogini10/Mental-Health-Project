from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def detailBlog(request, blog_id):
    data = {}

    blog_id = int(blog_id)

    post = Post.objects.get(id = blog_id)

    data = {
        'post': post
    }

    return render(request, 'blog/detailedblog.html', data)


def blogGrid(request):

    posts = Post.objects.all()

    data = {'posts': posts}

    return render(request, 'blog/bloggrid.html', data)