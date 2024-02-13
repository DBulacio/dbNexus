from django.contrib import admin

# Register your models here.
from .models import Client
admin.site.register(Client)

from .models import Product
admin.site.register(Product)
from .models import Stock
admin.site.register(Stock)

from .models import Balance
admin.site.register(Balance)
from .models import Service
admin.site.register(Service)
from .models import Order
admin.site.register(Order)
from .models import OrderHistory
admin.site.register(OrderHistory)