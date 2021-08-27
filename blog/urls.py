from django.urls import path
from .views import post_list, tag_detail, post_detail


app_name = 'blog'

urlpatterns = [
    path('', post_list, name = 'post_list'),
    path('posts/<int:pk>/', post_detail, name = "post_detail" ),
    path('tags/<int:pk>/', tag_detail, name = "tag_detail" ),
    ]