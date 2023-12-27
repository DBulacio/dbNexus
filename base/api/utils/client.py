from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import ClientSerializer, ClientDataSerializer
from base.models import Client, ClientData

def createClient(request):
  data = request.data

  client_instance = Client.objects.create_client(
    name = data["name"],
    dni  = data["dni"],
    cuil = data["cuil"],
    tel  = data["tel"],
  )

  client_serializer = ClientSerializer(client_instance, many=False)
  if(client_serializer.is_valid()):

    client_data_instance = ClientData.objects.create_client_data(
      client  = client_instance,
      dir     = data["dir"],
      num     = data["num"],
      postal  = data["postal"],
      country = data["country"],
      state   = data["state"],
    )

    client_data_serializer = ClientDataSerializer(client_data_instance, many=False)
    if(client_data_serializer.is_valid()):
      return Response(client_serializer.data, status=status.HTTP_200_OK)
    
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
      'client': client_data[0]['client'] if client_data else None,
      'country': client_data[0]['country'] if client_data else None,
      'state': client_data[0]['state'] if client_data else None,
    }

    combined_data_list.append(combined_data)

  return Response(combined_data_list, status=status.HTTP_200_OK)