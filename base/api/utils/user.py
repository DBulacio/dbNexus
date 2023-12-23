from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
# from ..serializers import UserSettingSerializer, UserSerializer
from ..serializers import UserSerializer
# from ...models import UserSetting, Company
from ...models import UserManager, User
# from django.contrib.auth.models import User, Group

def getUsers(request):
  users = get_list_or_404(User.objects.all())
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

def getUser(request, pk):
  try:
    user = User.objects.get(id=pk)

    user_serializer = UserSerializer(user, many=False)
    user_data = user_serializer.data

    return Response(user_data)

  except User.DoesNotExist:
    return Response({'error': 'User was not found!'}, status=404)
  
def createUser(request):
  data = request.data
    
  serializer = UserSerializer(data=data)
  if(serializer.is_valid()):
    user_instance = User.objects.create_user(
      email = data['email'],
      username = data['username'],
      first_name = data['first_name'],
      last_name = data['last_name'],
      password = data['password']
    )

    serializer = UserSerializer(user_instance, many=False)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateUser(request, pk):
  # Data has to look like this:
  # { "username": "testuser2", "password": "wut", "email": "test2@test.com", "first_name": "first_name2", "last_name": "last_name2" }
  data = request.data
  user = get_object_or_404(User, pk=pk)

  print(data)

  serializer = UserSerializer(instance=user, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    print('Validation Errors:', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
def deleteUser(request, pk):
  user = User.objects.get(id=pk)
  user.delete()
  
  return Response("User was deleted!")