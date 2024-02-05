from django.db import models
from django.utils import timezone
import datetime

class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance= models.IntegerField(default=0)
    modifiedDate= models.DateTimeField("last update")
    def __str__(self):
        return self.name
    def last_modiffied(self):
        return self.modifiedDate >= timezone.now() - datetime.timedelta(days=1)
    def current_balance(self):
        return self.balance
    
class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    credit= models.IntegerField(default=0)
    debit=models.IntegerField(default=0)
    modifiedDate= models.DateTimeField("transaction date time")
    def __str__(self):
        return self.customer.name
    def customer_id(self):
        return self.customer.id
    def last_modiffied(self):
        return self.modifiedDate >= timezone.now() - datetime.timedelta(days=1)
    def credit_amount(self):
        return self.credit
    def debit_amount(self):
        return self.debit