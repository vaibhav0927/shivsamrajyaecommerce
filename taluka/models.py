from django.db import models # type: ignore
from district.models import District

# Create your models here.
class Taluka(models.Model):
    taluka_id = models.AutoField(primary_key=True)
    taluka_name = models.CharField(max_length=255)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    class Meta:
        db_table = "tbl_taluka"


