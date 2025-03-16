from django.contrib import admin # type: ignore

from .models import Village

class VillageAdmin(admin.ModelAdmin):
    list_display=('village_id','village_name','village_slug','taluka_name')
    def taluka_name(self,obj):
        return obj.taluka.taluka_name 


admin.site.register(Village, VillageAdmin)