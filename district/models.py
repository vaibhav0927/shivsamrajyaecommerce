from django.db import models
from autoslug import AutoSlugField
from state.models import State  # Importing State model

<<<<<<< HEAD
from  state.models import state
from autoslug import AutoSlugField # type: ignore
 
# Create your models here.
class District(models.Model): 
=======
class District(models.Model):
>>>>>>> 0bc1a29285792c0513335d30e90703a7e53f9dac
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    district_slug = AutoSlugField(populate_from="district_name", unique=True)

    class Meta:
        db_table = "tbl_district"

    def __str__(self):
        return self.district_name
