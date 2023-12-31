from django.contrib import admin

# Register your models here.
from .models import Client
admin.site.register(Client)

from .models import Company
admin.site.register(Company)

from .models import Product
admin.site.register(Product)
from .models import Stock
admin.site.register(Stock)