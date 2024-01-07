from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import CompanySerializer
from base.models import Company

def createCompany(request):
  data = request.data

  serializer = CompanySerializer(data=data)
  if(serializer.is_valid()):
    company_instance = serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getCompanies(request):
  companies = get_list_or_404(Company.objects.filter(is_active=True))
  serializer = CompanySerializer(companies, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getCompany(request, pk):
  company = get_object_or_404(Company, pk=pk)
  serializer = CompanySerializer(company, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def deleteCompany(request, pk):
  company = get_object_or_404(Company, pk=pk)
  company.delete()

  return Response("Company was deleted!", status=status.HTTP_200_OK)

def updateCompany(request, pk):
  data = request.data
  company = get_object_or_404(Company, pk=pk)
  serializer = CompanySerializer(company, data=data)

  if(serializer.is_valid()):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getCompaniesByUser(request, pk):
  companies = get_list_or_404(Company.objects.filter(user=pk))
  serializer = CompanySerializer(companies, many=True)

  return Response(serializer.data, status=status.HTTP_200_OK)