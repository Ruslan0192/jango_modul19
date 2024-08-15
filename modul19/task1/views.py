import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.paginator import Paginator
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

        # выполнение ДЗ по администрированию
        buyer = Buyer.filter(username=username)
        if len(buyer) != 0:
            return HttpResponse('Пользователь с таким login уже существует!')


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

class HomePageView():
    # model = Syslog
    template_name = 'main.html'
    context_object_name = 'all_logs'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


def main(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'


    per_page = 10
    if "paginate_by" in request.POST:
        per_page = request.POST["paginate_by"]



    games = Game.objects.all()
    paginator = Paginator(games, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'per_page': per_page,
        'page_obj': page_obj,
    }


    return render(request, 'main.html', context=context)

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

def create_game():
    # временная функция для заполнения БД данными
    for i in range(1000):
        Game.objects.create(
            title=f'Game{i}',
            cost=10,
            size=20,
            description=f'Game{i}_description',
            age_limited=False,
        )



