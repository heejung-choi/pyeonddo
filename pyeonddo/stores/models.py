from django.db import models

class Store(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=500)
    time = models.CharField(max_length=200)
    atm = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    wine = models.CharField(max_length=200)
    lotto = models.CharField(max_length=200)
    bakery = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
