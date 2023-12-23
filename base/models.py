from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
  def _create_user(self, username, email, password, first_name, last_name, **extra_fields):
    if not email:
      raise ValueError("Email must be provided")
    if not password:
      raise ValueError('Password is not provided')

    user = self.model(
      email = self.normalize_email(email),
      username = username,
      password = password,
      first_name = first_name,
      last_name = last_name,
      **extra_fields
    )

    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self, username, email, password, first_name, last_name, **extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_active',True)
    extra_fields.setdefault('is_superuser',False)
    return self._create_user(username, email, password, first_name, last_name, **extra_fields)

  def create_superuser(self, username, email, password, first_name, last_name, **extra_fields):
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_active',True)
    extra_fields.setdefault('is_superuser',True)
    return self._create_user(username, email, password, first_name, last_name, **extra_fields)

class User(AbstractBaseUser):
  username = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=30)
  email = models.EmailField(verbose_name="email", max_length=60)
  date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
  last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'username'
  # REQUIRED_FIELDS = ['username', 'password', 'email', 'first_name', 'last_name']

  objects = UserManager()

  def __str__(self):
    return self.first_name + ", " + self.last_name
  
  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'