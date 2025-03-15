from django.contrib import admin
from .models import Taluka


# Register your models here.
class TalukaAdmin(admin.ModelAdmin):
    list_display = ('taluka_id','taluka_name')
    def district_name(self,obj):
        return obj.taluka.taluka_name
    def district_slug(self,obj):
        return obj.district.district_slug  
    district_name.short_description = "District Name"     
admin.site.register(Taluka,TalukaAdmin)

