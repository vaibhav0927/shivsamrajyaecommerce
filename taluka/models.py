from django.db import models # type: ignore

from  district.models import district
from autoslug import AutoSlugField # type: ignore

# Create your models here.
class Taluka(models.Model): 
    taluka_id = models.AutoField(primary_key=True)
    district=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    taluka_name = models.CharField(max_length=255)
    taluka_slug = AutoSlugField(populate_from="taluka_name", unique=True)
    class Meta:
        db_table = "tbl_taluka"
    def _str_(self):
        return self.taluka_name