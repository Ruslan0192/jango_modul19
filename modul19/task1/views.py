from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import *



def sign_up_by_html(request):

    if request.method == 'POST':
        # Получаем данные от пользователя
        # Обработка данных формы
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        balance = request.POST.get('balance')


        # проверка на совпадение паролей
        if password1 != password2:
            # Http ответ пользователю
            return HttpResponse('Пароли не совпадают! Заполните форму повторно')

        # проверка на совпадение login пользователей
        # загрузка из базы
        # buyer = Buyer.filter(username=username)
        # if buyer != None:

        try:
            buyer = Buyer.objects.get(username=username)
        except ObjectDoesNotExist:
            # запись нового покупателя в БД
            Buyer.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                password=password1,
                balance=balance
            )

            # return HttpResponse(f'Успешная регистрация! Приветствуем, {username}')
            # return render(request, 'main.html')
            return redirect('/main/')

        except MultipleObjectsReturned:
            print("Найдено более одного объекта")

        return HttpResponse('Пользователь с таким login уже существует!')


        # Если это запрос Get
    return render(request, 'registration_page.html')

# def sign_up_by_django(request):
#     if request.method == 'POST':
#         # Получаем данные от пользователя
#         form = RegistrationForm(request.POST)  # 2
#         # Validate the form
#         if form.is_valid():
#             # Обработка данных формы
#             username = form.cleaned_data['username'],
#             first_name = form.cleaned_data['first_name'],
#             last_name =form.cleaned_data['last_name'],
#             email = form.cleaned_data['email'],
#             age = 21 #int(form.cleaned_data['age']),
#             password1 = form.cleaned_data['password1'],
#             password2 = form.cleaned_data['password2'],
#             balance = 111.11 #float(form.cleaned_data['balance'])
#
#         # проверка на совпадение паролей
#         if password1 != password2:
#             # Http ответ пользователю
#             return HttpResponse('Пароли не совпадают! Заполните форму повторно')
#
#         # проверка на совпадение login пользователей
#         # загрузка из базы
#         # buyer = Buyer.filter(username=username)
#         # if buyer != None:
#
#         try:
#             buyer = Buyer.objects.get(username=username)
#         except ObjectDoesNotExist:
#             # запись нового покупателя в БД
#             Buyer.objects.create(
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 age=age,
#                 password=password1,
#                 balance=balance
#             )
#
#             # return HttpResponse(f'Успешная регистрация! Приветствуем, {username}')
#             # return render(request, 'main.html')
#             return redirect('/main/')
#
#         except MultipleObjectsReturned:
#             print("Найдено более одного объекта")
#
#         return HttpResponse('Пользователь с таким login уже существует!')
#
#         # Если это запрос Get
#     return render(request, 'registration_page.html')


def main(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    # list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    list = []
    games = Game.objects.all()

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'games': games,
    }

    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'main.html', context)


def page2(request):
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    # Напишем переменную, передающую имя второй страницы:
    return render(request, 'page2.html', context)


def page3(request):
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'list': list,
    }
    # Напишем переменную, передающую имя корзины:
    return render(request, 'page3.html', context)


