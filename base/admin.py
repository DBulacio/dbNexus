from django.contrib import admin

# Register your models here.
from .models import Company
admin.site.register(Company)

from .models import Module
admin.site.register(Module)
from .models import GroupModule
admin.site.register(GroupModule)

from .models import UserSetting
admin.site.register(UserSetting)