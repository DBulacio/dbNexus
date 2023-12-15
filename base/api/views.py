from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CompanySerializer, UserSerializer
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
    '/api/token',
    '/api/token/refresh',
  ]

  return Response(routes)

@api_view(['GET'])
def getCompanies(request):
   companies = Company.objects.all()
   serializer = CompanySerializer(companies, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
   users = UserSetting.objects.all()
   serializer = UserSerializer(users, many=True)
   return Response(serializer.data)