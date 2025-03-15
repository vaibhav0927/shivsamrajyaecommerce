from django.db import models # type: ignore
from autoslug import AutoSlugField  # type: ignore

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_fullNameEng = models.CharField(max_length=255)
    c_fullNameMarathi = models.CharField(max_length=255)
    c_mobile = models.CharField(max_length=255)
    c_birthDate = models.CharField(max_length=255)
    c_pinCode = models.CharField(max_length=255)
    c_email  = models.CharField(max_length=255)
    c_password = models.CharField(max_length=255)
    

# Create your models here.
