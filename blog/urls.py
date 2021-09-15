from django.urls import path

from .views import (
    post_list, 
    tag_detail, 
    post_detail, 
    tag_create, 
    post_create, 
    tag_edit, 
    post_edit, 
    post_delete,
    tag_delete,
    post_like,
    author_posts_list
)


app_name = 'blog'

urlpatterns = [
    path('', post_list, name = 'post_list'),
    path('posts/<int:pk>/', post_detail, name = "post_detail" ),
    path('posts/create', post_create, name = "post_create" ),
    path('posts/<int:pk>/update', post_edit, name = "post_edit" ),
    path('posts/<int:pk>/delete', post_delete, name = "post_delete" ),
    path('posts/liked/<int:pk>/', post_like, name = "post_like" ),
    path('author_posts/<int:user_id>/', author_posts_list, name = "author_posts_list" ),
    path('tags/<int:pk>/delete', tag_delete, name = "tag_delete" ),
    path('tags/<int:pk>/', tag_detail, name = "tag_detail" ),
    path('tags/create', tag_create, name = "tag_create" ),
    path('tags/<int:pk>/update', tag_edit, name = "tag_edit" ),
    path('tags/<int:pk>/update', tag_edit, name = "tag_edit" )
    ]