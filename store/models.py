from tkinter import CASCADE
from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=255,primary_key=True)
    title = models.CharField(max_length=255) # max lenght is mandatory
    slug = models.SlugField(default='-')
    description = models.TextField
    mobile = models.BigIntegerField
    price = models.DecimalField(max_digits=6, decimal_places=2) # the two arguments are always required in decimal field
    last_update = models.DateField(auto_now=True)
    collection = models.ForeignKey("Collection",on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_VALUES = [
        ('B',"BRONZE"),
        ('G',"GOLD")
    ]
    first_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) #only unique
    birth_date = models.DateField(null=True) # nullable
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_VALUES, default='B')

    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['first_name'])
        ]

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE, primary_key=True)# mandatory arguments

class Collection(models.Model):
    title = models.CharField(max_length=255)


