from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    # list_filter = ('name', 'phone')
    search_fields = ['name']

admin.site.register(Data, DataAdmin)