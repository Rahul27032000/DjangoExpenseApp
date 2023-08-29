from django.db import models
from django.contrib.auth.models import User

TYPE =(
    ('Positive','Positive'),
    ('Positive','Positive')
    )
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    income = models.FloatField()
    balance = models.FloatField(null=True)



class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=100, choices=TYPE)


    def __str__(self):
        return self.name
    