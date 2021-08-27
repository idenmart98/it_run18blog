from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

# Create your views here.

def post_list(request):
    tags = Tag.objects.all()
    posts = Post.objects.all()
    return render(request, 'post_list.html', context = {"posts":posts, "tags":tags})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    tags = Tag.objects.all()
    return render(request, 'post_detail.html', context = {'post': post, "tags":tags})


def tag_detail(request, pk):
    tags = Tag.objects.all()
    posts = Post.objects.filter(tags__id = pk)
    return render(request, 'post_list.html', context = {"posts":posts, "tags": tags})


