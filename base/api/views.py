from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .utils.user import updateUser, createUser, deleteUser, getUser, getUsers
from .utils.client import createClient, getClients, getClient
    
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
      'body': None,
      'description': 'Returns access and refresh token'
    },
    {
      'Endpoint': '/token/refresh/',
      'method': 'GET',
      'body': None,
      'description': 'Returns new access and refresh token. Blacklistes old refresh token.'
    },
    {
      'Endpoint': '/companies/',
      'method': 'GET',
      'body': None,
      'description': 'Returns an array of companies.'
    },
    {
      'Endpoint': '/users/',
      'method': 'GET',
      'body': None,
      'description': 'Returns an array of users.'
    },
    {
      'Endpoint': '/users/<str:pk>/',
      'method': 'GET',
      'body': None,
      'description': 'Returns a single user.'
    },
    {
      'Endpoint': '/users/create/',
      'method': 'POST',
      'body': {'body': ""},
      'description': 'Creates new user with data sent in post request.'
    },
    {
      'Endpoint': '/users/<str:pk>/update/',
      'method': 'PUT',
      'body': {'body': ""},
      'description': 'Updates an existing user with data sent in request.'
    },
    {
      'Endpoint': '/users/<str:pk>/delete/',
      'method': 'DELETE',
      'body': None,
      'description': 'Deletes an existing user.'
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

  # if(request.method == 'PUT'):
  #   return updateClient(request, pk)
  
  # if(request.method == 'DELETE'):
  #   return deleteClient(request, pk)
  
@api_view(['GET', 'POST'])
def allClients(request):
  if(request.method == 'GET'):
    return getClients(request)

  if(request.method == 'POST'):
    return createClient(request)