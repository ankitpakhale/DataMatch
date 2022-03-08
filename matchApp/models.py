from django.db import models

# Create your models here.

class Uploadcsv(models.Model):
    Hsn_code=models.CharField(max_length=20,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    CGst_rate=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    SGst_rate=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    IGst_rate=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    Per=models.CharField(max_length=30,null=True,blank=True)
    Rate=models.CharField(max_length=20,null=True,blank=True)
    user=models.CharField(max_length=30,null=True,blank=True)