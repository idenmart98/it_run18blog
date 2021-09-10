from django.urls import path

from .views import register_view, confirm_view, login_view, logout_view,reset_password

app_name = 'authe'

urlpatterns = [
    path('register/', register_view, name='registration'),
    path('confirm/<str:code>/', confirm_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reset/',reset_password,name='reset'),
    ]