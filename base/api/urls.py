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
  path('clients/<int:pk>/', views.individualClients, name='client'),
  path('clients/company/<int:company_id>/', views.clientsByCompany, name='clientsByCompany'),
  path('companies/', views.allCompanies, name='companies'),
  path('companies/<int:pk>/', views.individualCompanies, name='company'),
  path('companies/user/<int:user_id>/', views.companiesByUser, name='companiesByUser'),
  
  path('products/', views.allProducts, name='products'),
  path('products/<int:pk>/', views.individualProducts, name='product'),
  path('stock/', views.addStock, name='stock'),
  path('stock/bulk/', views.addBulStock, name='bulk-stock'),
  path('stock/<int:product_id>/', views.stockByProduct, name='stockByProduct'),
  
  path('services/', views.addService, name='add-service'),
  path('services/<int:pk>/', views.individualServices, name='service'),
  path('services/<int:company_id>/', views.getServicesByCompany, name='services'),

  path('balances/', views.addBalance, name='add-balance'),
  path('balances/<int:pk>/', views.individualBalances, name='balance'),
  path('balances/<int:client_id>/', views.getBalanceByClient, name='balances'),

  path('orders/', views.addOrder, name='add-order'),
  path('orders/<int:pk>/', views.individualOrders, name='order'),
  path('orders/<int:company_id>/', views.getOrdersByCompany, name='ordersByCompany'),
  path('orders/<int:client_id>/', views.getOrdersByClient, name='ordersByClient'),

  path('orderhistories/', views.addOrderHistory, name='add-orderhistory'),
  path('orderhistories/<int:pk>/', views.individualOrderHistories, name='orderhistory'),
  path('orderhistories/<int:company_id>/', views.getOrderHistoriesByCompany, name='orderhistoriesByCompany'),
  path('orderhistories/<int:client_id>/', views.getOrderHistoriesByClient, name='orderhistoriesByClient'),

  # country and state
  path('countries/', CountryListAPIView.as_view(), name='country-list'),
  path('states/', RegionListAPIView.as_view(), name='region-list'),
  # authentication
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]