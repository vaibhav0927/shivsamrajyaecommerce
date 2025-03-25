from django.contrib import admin # type: ignore

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display=('c_id','product_id','cart_quantity','cart_price')
    



admin.site.register(Cart, CartAdmin)

