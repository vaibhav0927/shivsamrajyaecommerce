from django.contrib import admin # type: ignore

from .models import Taluka

class TalukaAdmin(admin.ModelAdmin):
<<<<<<< HEAD

    list_display=('taluka_id','taluka_name')
    def district_name(self,obj):
        return obj.district.district_name 
    def district_slug(self,obj):
        return obj.district.district_slug  
    district_name.short_description = "District Name"   
admin.site.register(Taluka,TalukaAdmin)
=======
    list_display=('taluka_id','taluka_name','taluka_slug','district_name')
    def district_name(self,obj):
        return obj.district.district_name 


admin.site.register(Taluka, TalukaAdmin)
>>>>>>> 67874dc837de86263e425e4729e1a8a8c0070a62

