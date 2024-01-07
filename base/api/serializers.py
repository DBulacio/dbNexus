from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Client, Company, Product, Stock
from cities_light.models import Country, Region

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

class CompanySerializer(ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'
    extra_kwargs = {
      'name' : {'required': False},
      'user' : {'required': False},
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
      'company': {'required': False},
    }

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
    extra_kwargs = {
      'name':    {'required': False},
      'active':  {'required': False},
      'company': {'required': False},
    }

class StockSerializer(ModelSerializer):
  class Meta:
    model = Stock
    fields = '__all__'
    extra_kwargs = {
      'product':  {'required': False},
      'date_in':  {'required': False},
      'date_out': {'required': False},
    }

class CountrySerializer(ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'

class RegionSerializer(ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'