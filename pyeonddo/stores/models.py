from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=500)
    time = models.CharField(max_length=200)
    atm = models.BooleanField()
    medicine = models.BooleanField()
    wine = models.BooleanField()
    lotto = models.BooleanField()
    bakery = models.BooleanField()
    delivery = models.BooleanField()
