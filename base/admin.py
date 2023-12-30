from django.contrib import admin

# Register your models here.
from .models import Client
admin.site.register(Client)

from .models import Company
admin.site.register(Company)