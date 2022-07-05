from django.contrib import admin
from .models import Charginginfo

# Register your models here.

class CharginginfoAdmin(admin.ModelAdmin):
  list_display = ('cpname', 'username','energy',)

admin.site.register(Charginginfo, CharginginfoAdmin)
