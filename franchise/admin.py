from django.contrib import admin

from .models import Franchise
class FranchiseAdmin(admin.ModelAdmin):
    list_display=('franchise_id','franchise_name','franchise_slug')
admin.site.register(Franchise,FranchiseAdmin)
# Register your models here.
