from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Client

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      "password":         {'required': False},
      "last_login":       {'required': False},
      "is_superuser":     {'required': False},
      "username":         {'required': False},
      "first_name":       {'required': False},
      "last_name":        {'required': False},
      "email":            {'required': False},
      "is_staff":         {'required': False},
      "is_active":        {'required': False},
      "date_joined":      {'required': False},
      "groups":           {'required': False},
      "user_permissions": {'required': False},
    }

class ClientSerializer(ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'
    extra_kwargs = {
      'name':    {'required': False},
      'dni':     {'required': False},
      'cuil':    {'required': False},
      'tel':     {'required': False},
      'dir':     {'required': False},
      'num':     {'required': False},
      'postal':  {'required': False},
      'country': {'required': False},
      'state':   {'required': False},
    }