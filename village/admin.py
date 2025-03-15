from django.contrib import admin # type: ignore

<<<<<<< HEAD
=======

>>>>>>> 5b63a5203b2de69b79bfc3e2f45705f0a1f665dc
from .models import Village

class VillageAdmin(admin.ModelAdmin):
    list_display=('village_id','village_name','village_slug','taluka_name')
    def taluka_name(self,obj):
        return obj.taluka.taluka_name 


admin.site.register(Village, VillageAdmin)