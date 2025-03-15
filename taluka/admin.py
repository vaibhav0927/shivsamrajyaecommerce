from django.contrib import admin # type: ignore

from .models import Taluka

class TalukaAdmin(admin.ModelAdmin):
    list_display=('taluka_id','taluka_name','taluka_slug','district_name')
    def district_name(self,obj):
        return obj.district.district_name 


admin.site.register(Taluka, TalukaAdmin)


