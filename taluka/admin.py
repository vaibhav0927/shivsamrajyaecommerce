from django.contrib import admin # type: ignore

from .models import Taluka

class TalukaAdmin(admin.ModelAdmin):
    list_display=('taluka_id','taluka_name','taluka_slug','district_name')
    def district_name(self,obj):
        return obj.district.district_name 


<<<<<<< HEAD
admin.site.register(Taluka, TalukaAdmin)


=======
admin.site.register(Taluka, TalukaAdmin)
>>>>>>> 5b63a5203b2de69b79bfc3e2f45705f0a1f665dc
