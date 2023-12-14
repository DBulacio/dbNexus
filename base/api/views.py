from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProductSerializer
from base.models import Product
    
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
def getProducts(request):
   products = Product.objects.all()
   serializer = ProductSerializer(products, many=True)
   return Response(serializer.data)