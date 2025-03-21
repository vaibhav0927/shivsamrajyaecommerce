from django.contrib import admin

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','product_slug')
admin.site.register(Product,ProductAdmin)
# Register your models here.
