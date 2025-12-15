from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense (models.Model):
    description = models.TextField()
    data = models.DateTimeField()
    amount = models.BigIntegerField()
    user =models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
