from django.db import models
from autoslug import AutoSlugField
from tax.models import Tax

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255 , null=True)
    product_slug = AutoSlugField(populate_from="product_name", unique=True)
    tax=models.ForeignKey(Tax,null=True,on_delete=models.CASCADE)

    class Meta:
       db_table= "tbl_product"
# Create your models here.





