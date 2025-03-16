from django.contrib import admin # type: ignore

# Register your models here.
from .models import Brands

class BrandsAdmin(admin.ModelAdmin):
    list_display=('brands_id','brands_name')
    



admin.site.register(Brands, BrandsAdmin)

