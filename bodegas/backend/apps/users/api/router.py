from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.api.views import RegisterView, UserView, UserListView, UserDetailView, UserUpdateByIdView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),
    path('auth/users/', UserListView.as_view()),  # Ruta para listar usuarios
    path('auth/users/<int:id>/', UserDetailView.as_view()),  # Ruta para obtener usuario por ID
    path('auth/users/update/<int:id>/', UserUpdateByIdView.as_view()),  # Ruta para actualizar usuario por ID



]