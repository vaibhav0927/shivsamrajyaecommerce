from django.contrib import admin # type: ignore

from .models import District

class DistrictAdmin(admin.ModelAdmin):
    list_display=('district_id','district_name','district_slug','state_name')
    def state_name(self,obj):
        return obj.state.state_name 


admin.site.register(District, DistrictAdmin)