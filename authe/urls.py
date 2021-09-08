from django.urls import path

from .views import register_view, confirm_view

app_name = 'authe'

urlpatterns = [
    path('register/', register_view, name='registration'),
    path('confirm/<str:code>/', confirm_view, name='registration'),
    ]