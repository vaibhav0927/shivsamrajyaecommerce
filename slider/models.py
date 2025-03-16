from django.db import models # type: ignore

# Create your models here.

class Slider(models.Model):
    slider_id=models.AutoField(primary_key=True)
    slider_name=models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table="tbl_slider"
