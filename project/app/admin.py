from django.contrib import admin

from .models import Data, DType




# Register your models here.
class DTypeAdmin(admin.ModelAdmin):
  model = DType
  list_display = ('id', 'dtype', 'mode')

  fieldsets = [('DType', {'fields': ['dtype', 'mode']})]
  readonly_fields =  ['mode']

class DataAdmin(admin.ModelAdmin):
  model = Data

  list_display = ('id', 'date', 'dtype', 'value', 'mode')  
  readonly_fields =  ['mode']


admin.site.register(DType, DTypeAdmin)
admin.site.register(Data, DataAdmin)