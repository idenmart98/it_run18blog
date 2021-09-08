from django.shortcuts import redirect, render
from django.conf import settings

from .models import Author, ConfirmCode
from .forms import RegisterForm
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


