from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Client

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    
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