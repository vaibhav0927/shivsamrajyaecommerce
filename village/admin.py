from django.contrib import admin
from .models import Village

class VillageAdmin(admin.ModelAdmin):
    list_display = ('village_id', 'village_name', 'taluka', 'village_slug')
    list_filter = ('taluka',)
    search_fields = ('village_name',)

admin.site.register(Village, VillageAdmin)
