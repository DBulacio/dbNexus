from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CompanySerializer, UserSerializer
from base.models import Company, UserSetting
    
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

@api_view(['GET'])
def getCompanies(request):
  companies = Company.objects.all()
  serializer = CompanySerializer(companies, many=True)
  return Response(serializer.data)

# Simplify this in a separate file
# Users
@api_view(['GET'])
def getUsers(request):
  users = UserSetting.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
  user = UserSetting.objects.get(id=pk)
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
  data = request.data
    
  if User.objects.filter(username=data['username']).exists():
    return Response({"error": f"Username '{data['username']}' already exists."}, status=400)

  user_instance = User.objects.create(
    username=data['username'],
    password=data['password'],
    email=data['email'],
  )

  group_instance = Group.objects.get(id=1) # Seleccionar group
  company_instance = Company.objects.get(id=1) # Seleccionar company

  user_setting_instance = UserSetting.objects.create(
    user=user_instance,
    dni=data.get('dni', ''),
    firstName=data.get('firstName', ''),
    lastName=data.get('lastName', ''),
    phone=data.get('phone', ''),
    group_id=group_instance,
    company_id=company_instance,
    active=True,
  )
  serializer = UserSerializer(user_setting_instance, many=False)

  return Response(serializer.data)
  
@api_view(['PUT'])
def updateUser(request, pk):
  data = request.data
  user = UserSetting.objects.get(id=pk)
  serializer = UserSerializer(instance=user, data=data)
  
  if(serializer.is_valid()):
    serializer.save()
  else:
    print('Validation Errors:', serializer.errors)
    return Response(serializer.errors, status=400)
  
  return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
  user = UserSetting.objects.get(id=pk)
  user.delete()
  return Response("User was deleted!")