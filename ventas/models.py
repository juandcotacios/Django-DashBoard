from django.db import models

class VentasApple(models.Model):
    month = models.CharField(max_length=120)
    value= models.IntegerField()
    ubication = models.CharField(max_length= 120)

class VentasProductos(models.Model):
     product_type = models.CharField(max_length = 120)
     amount = models.IntegerField()   
# Create your models here.
