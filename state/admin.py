from django.contrib import admin
from .models import state
class stateAdmin(admin.ModelAdmin):
    list_display=('state_id','state_name','state_slug')
admin.site.register(state,stateAdmin)