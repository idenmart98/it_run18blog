from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .models import Author, ConfirmCode
from .forms import LoginForm, RegisterForm,ResetPassword
from django.contrib.auth.forms import UserCreationForm
from .utils import send_register_mail


def register_view(request):
    form = RegisterForm(request.POST or None)
    message = "Потча уже занята"
    if request.method == 'POST':
        author =  Author.objects.filter(email=request.POST['email'])
        if author:
            if author[0].verified:
                return render(request, 'register.html', {'form': form, 'message':message}) 
            code = ConfirmCode.objects.create(customer=author[0])
            message = f"{settings.SITE_URL}authe/confirm/{code.code}/"
            send_register_mail(message,author[0].email)
            message = "Вам отправлена ссылка"
        if form.is_valid(): 
            user = form.save()
            code = ConfirmCode.objects.create(customer=user)
            message = f"{settings.SITE_URL}authe/confirm/{code.code}/"
            send_register_mail(message,user.email)
            message = "Вам отправлена ссылка"
        return render(request, 'register.html', {'form': form, 'message':message})
    return render(request, 'register.html', {'form': form})

def confirm_view(request, code):
    code = ConfirmCode.objects.filter(code = code)
    form = RegisterForm(None)
    message = 'Код не найден'
    if code:
        user = code[0].customer
        user.verified = True
        user.save()
        code.delete()
        message = 'Ваша почта потверждена'
    return render(request, 'register.html', {'message':message, 'form': form})

def login_view(request):
    form  = LoginForm(request.POST or None)
    message = 'логин или пароль не верный'
    if request.method == 'POST' and form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            message = 'Все ок'
            login(request, user)
            return render(request, 'login.html', {'form':form, 'message':message})
    return render(request, 'login.html', {'form':form, 'message':message})

def logout_view(request):
    logout(request)
    return redirect('blog:post_list') 


def reset_password(request):
    form = ResetPassword(request.POST or None)
    message = ''
    if request.method == 'POST':
        author = Author.objects.filter(email=request.POST['email'])
        if author:
            code = ConfirmCode.objects.create(customer=author[0])
            msg = f"{settings.SITE_URL}authe/reset/{code.code}"
            send_register_mail(msg,author[0].email)
            message = 'Вам отправлена ссылка для сброса пароля'
            return render(request,'reset.html',{'form':form,'message':message})
        message = 'Такого пользователя нет'
        return render(request,'reset.html',{'form':form,'message':message})
    return render(request,'reset.html',{'form':form,'message':message})

