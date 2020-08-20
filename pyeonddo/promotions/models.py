from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    img = models.CharField(max_length=1000)
    event = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True)


