from django.db import models
from taluka.models import Taluka

# Create your models here.
class Village(models.Model):
    village_id = models.AutoField(primary_key=True)
    village_name = models.CharField(max_length=255)
    taluka = models.ForeignKey(Taluka,on_delete=models.CASCADE)
    class Meta:
        db_table = "tbl_village"


