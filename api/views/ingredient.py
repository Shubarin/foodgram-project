from rest_framework import permissions, viewsets

from api.serializers import IngredientSerializer
from recipes.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        mask = self.request.query_params.get('query', '').lower()
        return Ingredient.objects.filter(name__icontains=mask)
