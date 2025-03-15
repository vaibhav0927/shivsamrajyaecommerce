from django.contrib import admin # type: ignore
from .models import Slider
class SliderAdmin(admin.ModelAdmin):
    list_display=('slider_id','slider_name')
admin.site.register(Slider,SliderAdmin)
# Register your models here.
