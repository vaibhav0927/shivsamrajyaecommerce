from django.db import models # type: ignore

# Create your models here.
class Category(models.Model): 
    category_id = models.AutoField(primary_key=True)
    
    category_name = models.CharField(max_length=255)
   
    class Meta:
        db_table = "tbl_category"
    def _str_(self):
        return self.category_name
