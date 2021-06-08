from django.urls import include, path
from rest_framework import routers

from .views import (FavoriteViewSet, IngredientViewSet, RecipeViewSet,
                    UserViewSet)

router = routers.DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='FavoriteViewSet')
router.register(r'ingredients', IngredientViewSet,
                basename='IngredientViewSet')
router.register(r'recipes', RecipeViewSet, basename='RecipeViewSet')
router.register(r'users', UserViewSet, basename='UserViewSet')

urlpatterns = [path('v1/', include(router.urls)), ]
