from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import OrderStatus
from .serializers import OrderStatusSerializer

def getOrderStatuses(request):
  order_statuses = get_list_or_404(OrderStatus.objects.all())
  serializer = OrderStatusSerializer(order_statuses, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getOrderStatus(request, pk):
  order_status = get_object_or_404(OrderStatus, pk=pk)
  serializer = OrderStatusSerializer(order_status, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def createOrderStatus(request):
  data = request.data
  serializer = OrderStatusSerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateOrderStatus(request, pk):
  data = request.data
  order_status = get_object_or_404(OrderStatus, pk=pk)
  serializer = OrderStatusSerializer(instance=order_status, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteOrderStatus(request, pk):
  order_status = get_object_or_404(OrderStatus, pk=pk)
  order_status.delete()
  return Response("OrderStatus was deleted!", status=status.HTTP_200_OK)
