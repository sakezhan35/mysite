from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(
        redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('task_tracker/', include('task_tracker.urls',
                                  namespace='task_tracker')),
    path('api/task_tracker/', include('task_tracker.api.urls',
                                      namespace='api_task_tracker')),
]
