from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from base.models import Service, Company
from ..serializers import ServiceSerializer

def getServices(request, company_id):
  company = get_object_or_404(Company, id=company_id)
  services = get_list_or_404(Service.objects.filter(company=company))
  serializer = ServiceSerializer(services, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getService(request, pk):
  service = get_object_or_404(Service, pk=pk)
  serializer = ServiceSerializer(service, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def createService(request):
  data = request.data
  serializer = ServiceSerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateService(request, pk):
  data = request.data
  service = get_object_or_404(Service, pk=pk)
  serializer = ServiceSerializer(instance=service, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteService(request, pk):
  service = get_object_or_404(Service, pk=pk)
  service.delete()
  return Response("Service was deleted!", status=status.HTTP_200_OK)
