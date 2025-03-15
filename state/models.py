from django.db import models
from autoslug import AutoSlugField

class state(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=255)
    state_slug=AutoSlugField(populate_from="state_name",unique=True)
    class Meta:
        db_table="tbl_state"
    def __str__(self):
      return self.state_name



