from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Comment, Post, PostImage, Tag
from .forms import TagForm, PostForm, CommentForm, ImageForm

# Create your views here.

def post_list(request):
    tags = Tag.objects.all()
    posts = Post.objects.all()
    return render(request, 'post_list.html', context = {"posts":posts, "tags":tags})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    image = post.image.all()
    image = PostImage.objects.filter(post=post)
    post.views +=1
    post.save ()
    if request.method == 'POST':
        Comment.objects.create(
            name=form.data['name'], 
            email = form.data['email'], 
            text = form.data['text'],
            post=post
            )
        return redirect('blog:post_detail',pk=pk)
    tags = Tag.objects.all()
    return render(request, 'post_detail.html', context = {'post': post, "tags":tags , 'form':form, 'image': image})


def tag_detail(request, pk):
    tag = Tag.objects.get(id=pk)
    tags = Tag.objects.all()
    posts = Post.objects.filter(tags__id = pk)
    return render(request, 'post_list.html', context = {"posts":posts, "tags": tags, "tag": tag})

def tag_create(request):
    form = TagForm(request.POST or None)
    tags = Tag.objects.all()
    if request.method == 'POST':
        form.save()
        return redirect('blog:post_list')
    return render( request, 'tag_create.html', context= {'form':form, 'tags': tags})

def post_create(request):
    form = PostForm(request.POST or None)
    tags = Tag.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    return render( request, 'post_create.html', context= {'form':form, 'tags': tags})

def tag_edit(request, pk):
    tag =  Tag.objects.get(id=pk)
    form = TagForm(request.POST or None, instance=tag)
    tags = Tag.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    return render( request, 'tag_update.html', context= {'form':form, 'tags': tags, 'tag':tag})


def post_edit(request, pk):
    post =  Post.objects.get(id=pk)
    form = PostForm(request.POST or None, instance=post)
    tags = Tag.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    return render( request, 'post_update.html', context= {'form':form, 'tags': tags, 'post':post})

def post_delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('blog:post_list')

def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    count = post.liked
    post.liked=count+1
    post.save()
    return redirect('blog:post_detail', pk=pk)


def tag_delete(request, pk):
    Tag.objects.filter(pk=pk).delete()
    return redirect('blog:post_list')

# def post_image(request, pk):
#     post = Post.objects.get(pk=pk)
#     form = ImageForm(request.POST or None)
#     if request.method == 'POST':
#         Comment.objects.create(
#             image=form.data['image'], 
#             )
#         return redirect('blog:post_detail',pk=pk)
#     tags = Tag.objects.all()
#     return render(request, 'post_detail.html', context = {'post': post, "tags":tags , 'form':form})
