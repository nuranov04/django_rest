from apps.users.serializers import *
from apps.users.models import *
from rest_framework import viewsets
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
