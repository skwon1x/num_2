from django.shortcuts import render
#подключаем объект для выполнения http-запроса
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Домашка по 4 занятию')