from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email'
        ]


class TaskSerializer(serializers.ModelSerializer):
    observers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
