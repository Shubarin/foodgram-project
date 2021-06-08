from rest_framework import permissions, viewsets

from api.serializers import RecipeSerializer
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = Recipe.objects.all()
