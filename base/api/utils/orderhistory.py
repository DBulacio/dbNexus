from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import OrderHistory, Order, OrderStatus, Company
from .serializers import OrderHistorySerializer

def getOrderHistories(request, company_id):
  company = get_object_or_404(Company, id=company_id)
  order_histories = get_list_or_404(OrderHistory.objects.filter(company=company))
  serializer = OrderHistorySerializer(order_histories, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getOrderHistory(request, pk):
  order_history = get_object_or_404(OrderHistory, pk=pk)
  serializer = OrderHistorySerializer(order_history, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def createOrderHistory(request):
  data = request.data
  serializer = OrderHistorySerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateOrderHistory(request, pk):
  data = request.data
  order_history = get_object_or_404(OrderHistory, pk=pk)
  serializer = OrderHistorySerializer(instance=order_history, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteOrderHistory(request, pk):
  order_history = get_object_or_404(OrderHistory, pk=pk)
  order_history.delete()
  return Response("OrderHistory was deleted!", status=status.HTTP_200_OK)

def get_order_histories_by_order(request, order_id):
  order = get_object_or_404(Order, id=order_id)
  order_histories = get_list_or_404(OrderHistory.objects.filter(order=order))
  serializer = OrderHistorySerializer(order_histories, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)