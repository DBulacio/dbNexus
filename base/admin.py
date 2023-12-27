from django.contrib import admin

# Register your models here.
from .models import Client
from .models import ClientData

admin.site.register(Client)
admin.site.register(ClientData)