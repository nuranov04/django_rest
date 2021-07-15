from apps.users.models import *
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
