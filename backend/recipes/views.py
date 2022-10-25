from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator


RECIPE_COUNT: int = 10


def index(request):
    """Главная страница проекта Foodgram."""
    return HttpResponse('Главная страница проекта Foodgram')


def recipe_detail(request, recipe_id):
    """Страница отдельного рецепта."""
    return HttpResponse('Страница отдельного рецепта')
