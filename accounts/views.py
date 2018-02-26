from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail

from . import special_func
from .models import UserData
from .forms import SignUpForm, SignInForm


def login(request):
    return render(request, 'accounts/login.html', locals())


def registration(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        data = request.POST
        login1 = data['login']
        password = data['password']
        key = special_func.generate_key()
        user = UserData.objects.create(login=login1, password=password,
                                       created_data=datetime.now(), email_is_confirm=key)

        return render(request, 'accounts/confirm_email.html', locals())

    return render(request, 'accounts/login.html', locals())


def input(request):
    form = SignInForm(request.POST or None)

    if form.is_valid():
        return render(request, 'accounts/index.html', locals())

    return render(request, 'accounts/login.html', locals())


def getIndex(request):
    return render(request, 'index.html', locals())


def confirm_email(request, email, key):
    user = UserData.objects.get(email=email)
    email_is_confirm = user.email_is_confirm == key

    if email_is_confirm:
        user.email_is_confirm = None
        user.save()

    return render(request, 'accounts/confirm_email.html', locals())