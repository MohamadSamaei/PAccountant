from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense (models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user =models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.amount}-{self.date}"

class Income(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.amount}-{self.date}"