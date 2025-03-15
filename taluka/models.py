from django.db import models # type: ignore
from district.models import District
class Taluka(models.Model):
    taluka_id = models.AutoField(primary_key=True)

    taluka_name = models.CharField(max_length=255,null=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    class Meta:

      db_table = "tbl_taluka"


