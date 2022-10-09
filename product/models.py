from django.db import models

# Create your models here.


class Prods(models.Model):
    ref = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    store = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
