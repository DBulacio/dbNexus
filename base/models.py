from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Company(models.Model):
  name = models.TextField()

class Module(models.Model):
  name = models.CharField(max_length=15)
  url  = models.CharField(max_length=15)

class GroupModule(models.Model):
  group_id  = models.ForeignKey(Group, on_delete=models.CASCADE, default="0")
  module_id = models.ForeignKey(Module, on_delete=models.CASCADE, default="0")

class UserSetting(models.Model):
  user       = models.ForeignKey(User, on_delete=models.CASCADE)
  dni        = models.CharField(max_length=10, default="0")
  firstName  = models.TextField(blank=True)
  lastName   = models.TextField(blank=True)
  phone      = models.CharField(max_length=15)
  group_id   = models.ForeignKey(Group, on_delete=models.CASCADE, default="0")
  company_id = models.ForeignKey(Company, on_delete=models.CASCADE, default="0")
  active     = models.BooleanField(default=True)