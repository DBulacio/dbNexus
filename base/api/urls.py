from django.urls import path
from . import views
from .views import MyTokenObtainPairView
# authentication
from rest_framework_simplejwt.views import (
  TokenRefreshView,
)

urlpatterns = [
  path('', views.getRoutes),

  path('companies/', views.getCompanies, name='companies'),
  path('users/', views.getUsers, name='users'),
  path('users/create/', views.createUser, name='create-user'),
  path('users/<str:pk>/', views.getUser, name='user'),
  path('users/<str:pk>/update/', views.updateUser, name='update-user'),
  path('users/<str:pk>/delete/', views.deleteUser, name='delete-user'),
  # authentication
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]