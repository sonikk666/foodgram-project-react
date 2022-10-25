from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница рецепта
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
