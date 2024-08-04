from django.db import models


# Create your models here.


class Buyer(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=20, decimal_places=2)


class Game(models.Model):
    title = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

