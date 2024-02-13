from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from base.models import Order, Company
from ..serializers import OrderSerializer

def getOrder(request, pk):
  order = get_object_or_404(Order, pk=pk)
  serializer = OrderSerializer(order, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def createOrder(request):
  data = request.data
  serializer = OrderSerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateOrder(request, pk):
  data = request.data
  order = get_object_or_404(Order, pk=pk)
  serializer = OrderSerializer(instance=order, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteOrder(request, pk):
  order = get_object_or_404(Order, pk=pk)
  order.delete()
  return Response("Order was deleted!", status=status.HTTP_200_OK)

def get_orders_by_company(request, company_id):
  company = get_object_or_404(Company, id=company_id)
  orders = get_list_or_404(Order.objects.filter(company=company))
  serializer = OrderSerializer(orders, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def get_orders_by_client(request, client_id):
  client = get_object_or_404(Client, id=client_id)
  orders = get_list_or_404(Order.objects.filter(client=client))
  serializer = OrderSerializer(orders, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)