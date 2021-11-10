from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'task_tracker_api'

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
