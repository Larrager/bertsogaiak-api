from django.contrib import admin

from .models import Ofizioa

class OfizioaAdmin(admin.ModelAdmin):
    list_display = ('testu_laburra', 'metric', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('text', 'metric')

admin.site.register(Ofizioa, OfizioaAdmin)
