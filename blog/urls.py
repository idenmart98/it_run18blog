from django.urls import path
from .views import hello

app_name = 'blog'

urlpatterns = [
    path('', hello, name = 'hello'),
]