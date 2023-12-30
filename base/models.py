from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
  name = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
class Client(models.Model):
  name    = models.CharField(max_length=50)
  dni     = models.PositiveIntegerField()
  cuil    = models.PositiveBigIntegerField()
  tel     = models.CharField(max_length=50, null=True, blank=True)
  dir     = models.CharField(max_length=100, null=True, blank=True)
  num     = models.PositiveIntegerField(null=True, blank=True)
  postal  = models.CharField(max_length=20, null=True, blank=True)
  country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
  state   = models.ForeignKey('cities_light.Region', on_delete=models.SET_NULL, null=True, blank=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
