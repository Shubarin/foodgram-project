from rest_framework import permissions, viewsets

from api.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
