from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    join_date = models.DateField(default=date.today())
    is_subscribe = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


