from django.db import models # type: ignore
from state.models import state
from district.models import District
from taluka.models import Taluka
from village.models import Village
from franchise.models import Franchise
from autoslug import AutoSlugField  # type: ignore

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    state=models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    District=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    taluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,null=True)
    village=models.ForeignKey(Village,on_delete=models.CASCADE,null=True)
    franchise=models.ForeignKey(Franchise,on_delete=models.CASCADE,null=True)
    c_fullNameEng = models.CharField(max_length=255)
    c_fullNameMarathi = models.CharField(max_length=255)
    c_mobile = models.CharField(max_length=255)
    c_birthDate = models.CharField(max_length=255)
    c_pinCode = models.CharField(max_length=255)
    c_email  = models.CharField(max_length=255)
    c_password = models.CharField(max_length=255)
    

# Create your models here.
