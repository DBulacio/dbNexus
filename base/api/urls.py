from django.urls import path
from . import views
from .views import MyTokenObtainPairView, CountryListAPIView, RegionListAPIView
# authentication
from rest_framework_simplejwt.views import (
  TokenRefreshView,
)

urlpatterns = [
  path('', views.getRoutes),

  path('users/', views.allUsers, name='users'),
  path('users/<int:pk>/', views.individualUsers, name='user'),
  path('clients/', views.allClients, name='clients'),
  
  path('products/', views.allProducts, name='products'),
  path('products/<int:pk>/', views.individualProducts, name='product'),
  path('stock/', views.addStock, name='stock'),
  path('stock/bulk/', views.addBulStock, name='bulk-stock'),
  path('stock/<int:product_id>/', views.stockByProduct, name='stockByProduct'),
  
  path('services/', views.allServices, name='add-service'),
  path('services/<int:pk>/', views.individualServices, name='service'),

  path('balances/', views.addBalance, name='add-balance'),
  path('balances/<int:pk>/', views.individualBalances, name='balance'),
  path('balances/<int:client_id>/', views.getBalanceByClient, name='balances'),

  path('orders/', views.allOrders, name='add-order'),
  path('orders/<int:pk>/', views.individualOrders, name='order'),
  path('orders/<int:client_id>/', views.getOrdersByClient, name='ordersByClient'),

  path('orderhistories/', views.addOrderHistory, name='add-orderhistory'),
  path('orderhistories/<int:pk>/', views.individualOrderHistories, name='orderhistory'),
  path('orderhistories/<int:client_id>/', views.getOrderHistoriesByClient, name='orderhistoriesByClient'),

  # country and state
  path('countries/', CountryListAPIView.as_view(), name='country-list'),
  path('states/', RegionListAPIView.as_view(), name='region-list'),
  # authentication
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]