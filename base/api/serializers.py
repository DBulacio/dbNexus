from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Client, ClientData

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ClientDataSerializer(ModelSerializer):
  class Meta:
    model = ClientData
    fields = '__all__'

class ClientSerializer(ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'