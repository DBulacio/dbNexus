from django.urls import path
from . import views
from .views import MyTokenObtainPairView
# authentication
from rest_framework_simplejwt.views import (
  TokenRefreshView,
)

urlpatterns = [
  path('', views.getRoutes),

  path('users/', views.allUsers, name='users'),
  path('users/<str:pk>/', views.individualUsers, name='user'),
  path('clients/', views.allClients, name='clients'),
  path('clients/<str:pk>/', views.individualClients, name='client'),
  # authentication
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]