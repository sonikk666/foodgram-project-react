from django.urls import include, path
from rest_framework import routers

# from . import views
from .views import (IngredientViewSet, RecipeViewSet,  # SubscribeViewSet,
                    TagViewSet, UserViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('tag', TagViewSet)
router.register('ingredients', IngredientViewSet)
# router.register('subscribe', SubscribeViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('v1/recipes/<pk>/', views.get_recipe, name='id'),
]
