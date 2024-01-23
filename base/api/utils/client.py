from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import ClientSerializer
from base.models import Client

def createClient(request):
  # {
  # "name": "Client Test 0",
  # "dni": 1,
  # "cuil": 00000,
  # "tel": "11000000",
  # "dir": "casa test 0",
  # "num": 123,
  # "postal": "123",
  # "country": 10,
  # "state": 117,
  # "company": 1
  # }
  data = request.data

  serializer = ClientSerializer(data=data)
  if(serializer.is_valid()):
    client_instance = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getClients(request):
  clients = get_list_or_404(Client.objects.all())
  serializer = ClientSerializer(clients, many=True)

  return Response(serializer.data, status=status.HTTP_200_OK)

def getClient(request, pk):
  client = get_object_or_404(Client, pk=pk)
  serializer = ClientSerializer(client, many=False)

  return Response(serializer.data, status=status.HTTP_200_OK)

def deleteClient(request, pk):
  client = get_object_or_404(Client, pk=pk)
  client.delete()

  return Response("Client was deleted!", status=status.HTTP_200_OK)

def updateClient(request, pk):
  data = request.data
  client = get_object_or_404(Client, pk=pk)
  serializer = ClientSerializer(client, data=data)
        
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getClientsByCompany(request, company_id):
  clients = get_list_or_404(Client.objects.filter(company=company_id))
  serializer = ClientSerializer(clients, many=True)

  return Response(serializer.data, status=status.HTTP_200_OK)