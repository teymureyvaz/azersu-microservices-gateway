from django.contrib import admin
from django.contrib.auth.models import Permission
from  gateway.models import CompanyMonthsLimit
# Register your models here.

admin.site.register(Permission)
admin.site.register(CompanyMonthsLimit)