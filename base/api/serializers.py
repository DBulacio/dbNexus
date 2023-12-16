from rest_framework.serializers import ModelSerializer
from base.models import Company
from base.models import UserSetting
from django.contrib.auth.models import User

class CompanySerializer(ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class UserSettingSerializer(ModelSerializer):
  user = UserSerializer()
    
  class Meta:
    model = UserSetting
    fields = '__all__'

  def update(self, instance, validated_data):
    user_data = validated_data.pop('user', None)
    instance = super().update(instance, validated_data)

    if user_data:
      user_instance = instance.user
      for key, value in user_data.items():
        setattr(user_instance, key, value)
      user_instance.save()

    return instance