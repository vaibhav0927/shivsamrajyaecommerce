from django.db import models

from  state.models import state
from autoslug import AutoSlugField

# Create your models here.
class District(models.Model): 
    district_id = models.AutoField(primary_key=True)
    state=models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    district_name = models.CharField(max_length=255)
    district_slug = AutoSlugField(populate_from="district_name", unique=True)
    class Meta:
        db_table = "tbl_district"
    def _str_(self):
        return self.district_name