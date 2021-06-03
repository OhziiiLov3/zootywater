from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.views.generic.base import TemplateView

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    join_date = models.DateField(default=date.today())
    is_subscribe = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Order(models.Model):

    email = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.email


