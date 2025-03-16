from django.contrib import admin # type: ignore
<<<<<<< HEAD
=======

>>>>>>> 67874dc837de86263e425e4729e1a8a8c0070a62
from .models import Village

class VillageAdmin(admin.ModelAdmin):
    list_display=('village_id','village_name','village_slug','taluka_name')
    def taluka_name(self,obj):
        return obj.taluka.taluka_name 


admin.site.register(Village, VillageAdmin)