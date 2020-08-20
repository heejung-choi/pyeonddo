from django.db import models
from django.contrib.auth.models import AbstractUser
from stores.models import Store

# class Partner(AbstractUser):
#     phone = models.CharField(max_length=200)
#     name_kr = models.CharField(max_length=100)
#     store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, null=True)


class User(AbstractUser):
    phone = models.CharField(max_length=200)
    name_kr = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    prefer_store = models.CharField(max_length=100, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, null=True)
    