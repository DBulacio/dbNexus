from rest_framework.response import Response
from ..serializers import UserSettingSerializer, UserSerializer
from ...models import UserSetting
from django.contrib.auth.models import User, Group

def getUsers(request):
  users = UserSetting.objects.all()
  serializer = UserSettingSerializer(users, many=True)
  return Response(serializer.data)

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
  
def deleteUser(request, pk):
  userSetting = UserSetting.objects.get(id=pk)
  user = User.objects.get(id=userSetting.user.id)
  user.delete()
  userSetting.delete()
  
  return Response("User was deleted!")