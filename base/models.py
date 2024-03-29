from django.db import models
from django.contrib.auth.models import User
  
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

class Product(models.Model):
  name    = models.CharField(max_length=50)
  is_active  = models.BooleanField(default=True)

class Stock(models.Model):
  product  = models.ForeignKey(Product, on_delete=models.CASCADE)
  date_in  = models.DateField(auto_now_add=True)
  date_out = models.DateField(null=True, blank=True, default=None)

class Balance(models.Model):
  client = models.ForeignKey('Client', on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  IN = 'IN'
  OUT = 'OUT'
  TRANSACTION_CHOICES = [
      (IN, 'In'),
      (OUT, 'Out'),
  ]
  transaction_type = models.CharField(
      max_length=3,
      choices=TRANSACTION_CHOICES,
      default=IN,
  )
  timestamp = models.DateTimeField(auto_now_add=True)
  transaction_reference = models.CharField(max_length=255, null=True, blank=True)
  currency = models.CharField(max_length=3)

class Service(models.Model):
  name = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)

class Order(models.Model):
  class OrderStatus(models.TextChoices):
    PENDING    = 'Pending', 'Pending'
    ACCEPTED   = 'Accepted', 'Accepted'
    REJECTED   = 'Rejected', 'Rejected'
    PROCESSING = 'Processing', 'Processing'
    COMPLETED  = 'Completed', 'Completed'
    DELIVERED  = 'Delivered', 'Delivered'
    CANCELLED  = 'Cancelled', 'Cancelled'
    REOPENED   = 'Reopened', 'Reopened'
  
  client = models.ForeignKey('Client', on_delete=models.CASCADE)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)
  cur_status = models.CharField(
    max_length=20,
    choices=OrderStatus.choices,
    default=OrderStatus.PENDING
  )
  total_cost = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField(auto_now_add=True)

class OrderHistory(models.Model):
  class OrderStatus(models.TextChoices):
    PENDING    = 'Pending', 'Pending'
    ACCEPTED   = 'Accepted', 'Accepted'
    REJECTED   = 'Rejected', 'Rejected'
    PROCESSING = 'Processing', 'Processing'
    COMPLETED  = 'Completed', 'Completed'
    DELIVERED  = 'Delivered', 'Delivered'
    CANCELLED  = 'Cancelled', 'Cancelled'
    REOPENED   = 'Reopened', 'Reopened'

  order = models.ForeignKey('Order', on_delete=models.CASCADE)
  status = models.CharField(
    max_length=20,
    choices=OrderStatus.choices
  )
  client = models.ForeignKey('Client', on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
