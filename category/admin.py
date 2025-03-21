from django.contrib import admin # type: ignore

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_id','category_name')
    
admin.site.register(Category, CategoryAdmin)


