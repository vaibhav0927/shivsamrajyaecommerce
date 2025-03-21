from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore
from state.models import State  # Importing State model

<<<<<<< HEAD

 
# Create your models here. 
class District(models.Model):
=======
 
# Create your models here.

class District(models.Model):

>>>>>>> 418d82337c0c3efc68bc38801b9d6e9805136440
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    district_slug = AutoSlugField(populate_from="district_name", unique=True)

    class Meta:
        db_table = "tbl_district"

    def __str__(self):
        return self.district_name
