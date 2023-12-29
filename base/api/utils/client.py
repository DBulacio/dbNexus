from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import ClientSerializer, ClientDataSerializer
from base.models import Client, ClientData

def createClient(request):
#   {
#   "name": "Client Test 9",
#   "dni": 9,
#   "cuil": 90909,
#   "tel": "11000009",
#   "dir": "casa test 9",
#   "num": 123,
#   "postal": "123",
#   "country": 10,
#   "state": 117
#   }
  data = request.data

  client = {
    "name" : data["name"],
    "dni"  : data["dni"],
    "cuil" : data["cuil"],
    "tel"  : data["tel"],
  }

  client_serializer = ClientSerializer(data=client)
  if(client_serializer.is_valid()):
    client_instance = client_serializer.save()

    client_data = {
      "client"  : client_instance.pk,
      "dir"     : data["dir"],
      "num"     : data["num"],
      "postal"  : data["postal"],
      "country"  : data["country"],
      "state"  : data["state"],
    }

    client_data_serializer = ClientDataSerializer(data=client_data)

    if(client_data_serializer.is_valid()):
      client_data_instance = client_data_serializer.save()
      return Response(ClientDataSerializer(client_data_instance).data, status=status.HTTP_200_OK)
    
    return Response("There was an error creating ClientData", status=status.HTTP_400_BAD_REQUEST)
  return Response("There was an error creating Client", status=status.HTTP_400_BAD_REQUEST)

def getClients(request):
  clients = get_list_or_404(Client.objects.all())
  client_serializer = ClientSerializer(clients, many=True)

  client_datas = get_list_or_404(ClientData.objects.all())
  client_data_serializer = ClientDataSerializer(client_datas, many=True)

  combined_data_list = []

  for client in clients:
    client_id = client.id
    client_data = [data for data in client_data_serializer.data if data['client'] == client_id]

    # Combine client and clientdata
    combined_data = {
      'id': client.id,
      'name': client.name,
      'dni': client.dni,
      'cuil': client.cuil,
      'tel': client.tel,
      'dir': client_data[0]['dir'] if client_data else None,
      'num': client_data[0]['num'] if client_data else None,
      'postal': client_data[0]['postal'] if client_data else None,
      'country': client_data[0]['country'] if client_data else None,
      'state': client_data[0]['state'] if client_data else None,
    }

    combined_data_list.append(combined_data)

  return Response(combined_data_list, status=status.HTTP_200_OK)

def getClient(request, pk):
  client = get_object_or_404(Client, pk=pk)
  client_serializer = ClientSerializer(client, many=False)

  # There may be cases where we don't have client_data to display.
  try:
    client_data = ClientData.objects.get(client=pk)
    client_data_serializer = ClientDataSerializer(client_data, many=False)
  except ClientData.DoesNotExist:
    client_data_serializer = None

  combined_data = {
    'id': client_serializer.data['id'],
    'name': client_serializer.data['name'],
    'dni': client_serializer.data['dni'],
    'cuil': client_serializer.data['cuil'],
    'tel': client_serializer.data['tel'],
    'dir': client_data_serializer.data['dir'] if client_data_serializer else None,
    'num': client_data_serializer.data['num'] if client_data_serializer else None,
    'postal': client_data_serializer.data['postal'] if client_data_serializer else None,
    'country': client_data_serializer.data['country'] if client_data_serializer else None,
    'state': client_data_serializer.data['state'] if client_data_serializer else None,
  }

  return Response(combined_data, status=status.HTTP_200_OK)

def deleteClient(request, pk):
  client = get_object_or_404(Client, pk=pk)
  client.delete()

  try:
    client_data = ClientData.objects.get(client=pk)
    client_data.delete()
  except ClientData.DoesNotExist:
    pass

  return Response("Client was deleted!", status=status.HTTP_200_OK)