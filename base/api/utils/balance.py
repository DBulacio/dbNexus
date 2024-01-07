from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Balance
from .serializers import BalanceSerializer

# def getBalances(request):
#   balances = get_list_or_404(Balance.objects.all())
#   serializer = BalanceSerializer(balances, many=True)
#   return Response(serializer.data, status=status.HTTP_200_OK)

def getBalance(request, client_id):
  balances = get_list_or_404(Balance.objects.filter(client__id=client_id))
  serializer = BalanceSerializer(balances, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def createBalance(request):
  data = request.data
  serializer = BalanceSerializer(data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateBalance(request, pk):
  data = request.data
  balance = get_object_or_404(Balance, pk=pk)
  serializer = BalanceSerializer(instance=balance, data=data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteBalance(request, pk):
  balance = get_object_or_404(Balance, pk=pk)
  balance.delete()
  return Response("Balance was deleted!", status=status.HTTP_200_OK)
