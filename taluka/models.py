from django.db import models # type: ignore




from  district.models import District
from autoslug import AutoSlugField # type: ignore

# Create your models here.
class Taluka(models.Model): 
    taluka_id = models.AutoField(primary_key=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    taluka_name = models.CharField(max_length=255,null=True)
    taluka_slug = AutoSlugField(populate_from="taluka_name", unique=True,null=True, blank=True)
    class Meta:
        db_table = "tbl_taluka"
    def __str__(self):
        return self.taluka_name

