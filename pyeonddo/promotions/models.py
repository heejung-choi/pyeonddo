from django.db import models
from accounts.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    img = models.CharField(max_length=1000)
    event = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True)


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='partner')
    product = models.ManyToManyField(Product,related_name='event_product',null=True)
    