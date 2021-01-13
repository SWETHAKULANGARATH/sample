from django.db import models

# Create your models here.
class tbl_user(models.Model):
    name = models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_user"
        
class tbl_login(models.Model):
    user_id = models.CharField(max_length=30)
    lpassword =models.CharField(max_length=30)
   
    class Meta:
        db_table = "tbl_login"
        