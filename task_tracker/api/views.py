from rest_framework import viewsets
from .serializers import TaskSerializer
from ..models import Task


# Task list, retrieve, create ,update api
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
