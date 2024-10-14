from django.db import models

# Create your models here.

class Pickup_form(models.Model):
    pickup=models.CharField(max_length=100)
    dropoff=models.CharField(max_length=100)
    pickupdate=models.CharField(max_length=100)
    dropoffdate=models.CharField(max_length=100)
    pickuptime=models.CharField(max_length=100)

class Contact(models.Model):
    cname=models.CharField(max_length=100)
    cemail=models.CharField(max_length=100)
    csubject=models.CharField(max_length=100)
    cmessage=models.CharField(max_length=100)
    ctext=models.CharField(max_length=100)

class Customer(models.Model):
	customer_name=models.CharField(max_length=100)
	customer_mobile=models.CharField(max_length=15)
	customer_email=models.CharField(max_length=15)
	customer_password=models.CharField(max_length=15)