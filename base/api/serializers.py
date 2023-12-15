from rest_framework.serializers import ModelSerializer
from base.models import Company
from base.models import UserSetting

class CompanySerializer(ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'

class UserSerializer(ModelSerializer):
  class Meta:
    model = UserSetting
    fields = '__all__'