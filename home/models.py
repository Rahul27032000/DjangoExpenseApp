from django.db import models
from django.contrib.auth.models import User

TYPE =(
    ('Positive','Positive'),
    ('Negative', 'Negative')
    )
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    income = models.FloatField()
    expenses = models.FloatField(default=0)
    balance = models.FloatField(null=True,blank=True,default=None)




    def __str__(self):
        return self.user.username
    



class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)


    def __str__(self):
        return self.name
    