from django.contrib import admin # type: ignore
from .models import Village


# Register your models here.
class VillageAdmin(admin.ModelAdmin):
    list_display = ('village_id','village_name')
    def taluka_name(self,obj):
        return obj.taluka.taluka_name
    def taluka_slug(self,obj):
        return obj.taluka.taluka_slug  
    taluka_name.short_description = "Taluka Name"     
admin.site.register(Village,VillageAdmin)

