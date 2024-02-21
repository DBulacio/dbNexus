from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import UserSerializer
from django.contrib.auth.models import User, Group

def getUsers(request):
  users = get_list_or_404(User.objects.filter(is_active=True))
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getUser(request, pk):
  user = get_object_or_404(User, pk=pk)

  user_serializer = UserSerializer(user, many=False)
  user_data = user_serializer.data

  return Response(user_data, status=status.HTTP_200_OK)
  
def createUser(request):
    #   {
    #     "password": "test",
    #     "username": "client",
    #     "firstName": "client",
    #     "lastName": "test",
    #     "email": "daniel@client.com",
    #     "group": 1
    # }
  data = request.data

  user_instance = User.objects.create_user(
    username=data['username'],
    password=data['password'],
    email=data['email'],
    first_name=data['firstName'],
    last_name=data['lastName'],
  )

  group_id = data['group']
  try:
    group = Group.objects.get(id=group_id)
    user_instance.groups.add(group)
  except Group.DoesNotExist:
    return Response("Group does not exist", status=status.HTTP_400_BAD_REQUEST)

  serializer = UserSerializer(user_instance, many=False)
  if serializer.is_valid:
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  return Response("There was an error creating the user", status=status.HTTP_400_BAD_REQUEST)

def updateUser(request, pk):
  data = request.data
  user = User.objects.get(id=pk)

  serializer = UserSerializer(instance=user, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    print('Validation Errors:', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteUser(request, pk):
  user = get_object_or_404(User, pk=pk)
  user.delete()
  
  return Response("User was deleted!", status=status.HTTP_200_OK)

def getClients(request):
  # Filter users by group 'client'
  clients = get_list_or_404(User.objects.filter(is_active=True, groups__name='client'))
  serializer = UserSerializer(clients, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)