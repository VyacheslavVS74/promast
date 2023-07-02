from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def register_users(request):
    page = 'register'
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Аккаунт создан')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'При регистрации произошла ошибка')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login.html', context)


def login_users(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Такого логина не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Не верное имя пользователя или пароль')

    return render(request, 'users/login.html')


def logout_users(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта')
    return redirect('login')
