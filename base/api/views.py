from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from cities_light.models import Country, Region
from .serializers import CountrySerializer, RegionSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .utils.user import updateUser, createUser, deleteUser, getUser, getUsers
from .utils.client import createClient, getClients, getClient, deleteClient, updateClient, getClientsByCompany
from .utils.company import createCompany, getCompanies, getCompany, deleteCompany, updateCompany, getCompaniesByUser
from .utils.product import createProduct, getProducts, getProduct, deleteProduct, updateProduct, addBulkStock, addManualStock, getStockByProduct, takeStock
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['username'] = user.username
    # ...

    return token
class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
    {
      'Endpoint': '/token/',
      'method': 'GET',
      'description': 'Returns access and refresh token'
    },
    {
      'Endpoint': '/token/refresh/',
      'method': 'GET',
      'description': 'Returns new access and refresh token. Blacklistes old refresh token.'
    },
    {
      'Endpoint': '/users/',
      'method': 'GET',
      'description': 'Returns an array of users or creates a new user.'
    },
    {
      'Endpoint': '/users/<str:pk>/',
      'method': 'GET',
      'description': 'Returns, updates or deletes a single user.'
    },
    {
      'Endpoint': '/clients/',
      'method': 'GET',
      'description': 'Returns an array of clients or creates a new client.'
    },
    {
      'Endpoint': '/clients/<str:pk>/',
      'method': 'GET',
      'description': 'Returns, updates or deletes a single client.'
    },
    {
      'Endpoint': '/clients/company/<str:pk>/',
      'method': 'GET',
      'description': 'Returns an array of clients of company.'
    },
    {
      'Endpoint': '/companies/',
      'method': 'GET',
      'description': 'Returns an array of companies or creates a new company.'
    },
    {
      'Endpoint': '/companies/<str:pk>/',
      'method': 'GET',
      'description': 'Returns, updates or deletes a single company.'
    },
    {
      'Endpoint': '/companies/user/<str:pk>/',
      'method': 'GET',
      'description': 'Returns an array of companies of user.'
    },
    {
      'Endpoint': '/products/',
      'method': 'GET',
      'description': 'Returns an array of products or creates a new product.'
    },
    {
      'Endpoint': '/products/<str:pk>/',
      'method': 'GET',
      'description': 'Returns, updates or deletes a single product.'
    },
    {
      'Endpoint': '/stock/',
      'method': 'GET',
      'description': 'Creates one row of stock.'
    },
    {
      'Endpoint': '/stock/bulk/',
      'method': 'GET',
      'description': 'Creates rows of stock of product.'
    },
    {
      'Endpoint': '/stock/<str:pk>/',
      'method': 'GET',
      'description': 'Returns count of rows of stock, or updates date_out of stock.'
    },
  ]

  return Response(routes)

# Users
@api_view(['GET', 'PUT', 'DELETE'])
def individualUsers(request, pk):
  if(request.method == 'GET'):
    return getUser(request, pk)

  if(request.method == 'PUT'):
    return updateUser(request, pk)
  
  if(request.method == 'DELETE'):
    return deleteUser(request, pk)

@api_view(['GET', 'POST'])
def allUsers(request):
  if(request.method == 'GET'):
    return getUsers(request)

  if(request.method == 'POST'):
    return createUser(request)
  
# Clients
@api_view(['GET', 'PUT', 'DELETE'])
def individualClients(request, pk):
  if(request.method == 'GET'):
    return getClient(request, pk)

  if(request.method == 'PUT'):
    return updateClient(request, pk)
  
  if(request.method == 'DELETE'):
    return deleteClient(request, pk)
  
@api_view(['GET', 'POST'])
def allClients(request):
  if(request.method == 'GET'):
    return getClients(request)

  if(request.method == 'POST'):
    return createClient(request)

@api_view(['GET'])
def clientsByCompany(request, pk):
  return getClientsByCompany(request, pk)

# Companies
@api_view(['GET', 'PUT', 'DELETE'])
def individualCompanies(request, pk):
  if(request.method == 'GET'):
    return getCompany(request, pk)

  if(request.method == 'PUT'):
    return updateCompany(request, pk)
  
  if(request.method == 'DELETE'):
    return deleteCompany(request, pk)
  
@api_view(['GET', 'POST'])
def allCompanies(request):
  if(request.method == 'GET'):
    return getCompanies(request)

  if(request.method == 'POST'):
    return createCompany(request)
  
@api_view(['GET'])
def companiesByUser(request, pk):
  return getCompaniesByUser(request, pk)

# Products
@api_view(['GET', 'POST'])
def allProducts(request):
  if(request.method == 'GET'):
    return getProducts(request)

  if(request.method == 'POST'):
    return createProduct(request)

@api_view(['GET', 'PUT', 'DELETE'])
def individualProducts(request, pk):
  if(request.method == 'GET'):
    return getProduct(request, pk)

  if(request.method == 'PUT'):
    return updateProduct(request, pk)
  
  if(request.method == 'DELETE'):
    return deleteProduct(request, pk)

# Stock
@api_view(['GET', 'PUT'])
def stockByProduct(request, pk):
  if(request.method == 'GET'):
    return getStockByProduct(request, pk)
  if(request.method == 'PUT'):
    return takeStock(request, pk)

@api_view(['POST'])
def addStock(request):
  return addManualStock(request)
@api_view(['POST'])
def addBulStock(request):
  return addBulkStock(request)

# Country and State
class CountryListAPIView(generics.ListAPIView):
  queryset = Country.objects.all()
  serializer_class = CountrySerializer

class RegionListAPIView(generics.ListAPIView):
  queryset = Region.objects.all()
  serializer_class = RegionSerializer