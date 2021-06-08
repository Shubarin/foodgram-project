from api.models import Favorite
from api.serializers import CustomModelSerializer


class FavoriteSerializer(CustomModelSerializer):
    class Meta:
        model = Favorite
        fields = ('recipe', )
