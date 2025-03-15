from django.db import models # type: ignore

from  taluka.models import Taluka
from autoslug import AutoSlugField # type: ignore

# Create your models here.
class Village(models.Model): 
    village_id = models.AutoField(primary_key=True)
    taluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,null=True)
    village_name = models.CharField(max_length=255)
    village_slug = AutoSlugField(populate_from="village_name", unique=True,null=True, blank=True)
    class Meta:
        db_table = "tbl_village"
    def __str__(self):
        return self.village_name