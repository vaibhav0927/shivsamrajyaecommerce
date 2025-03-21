from django.db import models
from autoslug import AutoSlugField
class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=255 , null=True)
    tax_slug = AutoSlugField(populate_from="tax_name", unique=True)
    class Meta:
       db_table= "tbl_tax"
