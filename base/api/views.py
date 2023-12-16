from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CompanySerializer, UserSettingSerializer, UserSerializer
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
  serializer = UserSettingSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
  try:
    # Get User and UserSetting instances based on the provided primary key (pk)
    user_setting = UserSetting.objects.get(id=pk)

    # Serialize UserSetting data
    user_setting_serializer = UserSettingSerializer(user_setting, many=False)
    user_setting_data = user_setting_serializer.data

    return Response(user_setting_data)

  except UserSetting.DoesNotExist:
    # Handle the case where either User or UserSetting does not exist for the provided pk
    return Response({'error': 'UserSetting not found'}, status=404)

@api_view(['POST'])
def createUser(request):
  data = request.data
    
  if User.objects.filter(username=data['username']).exists():
    return Response({"error": f"Username '{data['username']}' already exists."}, status=400)

  user_instance = User.objects.create_user(
    username=data['username'],
    password=data['password'],
    email=data['email'],
    first_name=data['firstName'],
    last_name=data['lastName'],
  )

  group_instance = Group.objects.get(id=1) # Seleccionar group
  company_instance = Company.objects.get(id=1) # Seleccionar company

  user_setting_instance = UserSetting.objects.create(
    user=user_instance,
    dni=data.get('dni', ''),
    phone=data.get('phone', ''),
    group_id=group_instance,
    company_id=company_instance,
  )
  serializer = UserSettingSerializer(user_setting_instance, many=False)

  return Response(serializer.data)
  
@api_view(['PUT'])
def updateUser(request, pk):
  try:
    data = request.data
    user_setting = UserSetting.objects.get(id=pk)

    # Update UserSetting fields
    serializer = UserSettingSerializer(instance=user_setting, data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print('Validation Errors:', serializer.errors)
      return Response(serializer.errors, status=400)

  except UserSetting.DoesNotExist:
    return Response({'error': 'UserSetting not found'}, status=404)

@api_view(['DELETE'])
def deleteUser(request, pk):
  userSetting = UserSetting.objects.get(id=pk)
  user = User.objects.get(id=userSetting.user.id)
  user.delete()
  userSetting.delete()
  
  return Response("User was deleted!")