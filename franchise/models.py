from django.db import models
from autoslug import AutoSlugField
class Franchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    franchise_name = models.CharField(max_length=255 , null=True)
    franchise_slug = AutoSlugField(populate_from="franchise_name", unique=True)
    class Meta:
       db_table= "tbl_franchise"
# Create your models here.
