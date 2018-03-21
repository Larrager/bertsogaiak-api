from django.contrib import admin

from .models import Bakarkakoa

class BakarkakoaAdmin(admin.ModelAdmin):
    list_display = ('testu_laburra', 'type', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('text', 'type')

admin.site.register(Bakarkakoa, BakarkakoaAdmin)
