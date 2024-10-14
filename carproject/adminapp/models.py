from django.db import models

# Create your models here.

class Basic_info(models.Model):
    office_address=models.CharField(max_length=100)
    office_email=models.CharField(max_length=100)
    office_mobile=models.CharField(max_length=15)
    office_facebook=models.CharField(max_length=30)
    office_instagram=models.CharField(max_length=30)
    office_linkedin=models.CharField(max_length=30)

class HomePage(models.Model):
    himg=models.ImageField(upload_to="static/")
    hheading=models.CharField(max_length=100)
    hparag=models.CharField(max_length=100)
    aimg=models.ImageField(upload_to="static/") 

class Carinfo(models.Model):
    cname=models.CharField(max_length=20)
    cprice=models.CharField(max_length=20)
    cimg=models.ImageField(upload_to='static/') 

class Aboutinfo(models.Model):
    abheading=models.CharField(max_length=100)
    abtext=models.CharField(max_length=1000)

class TestInfo(models.Model):
    timg=models.ImageField(upload_to='static/')
    tinfo=models.CharField(max_length=300)
    tname=models.CharField(max_length=30)
    tpos=models.CharField(max_length=40)

class BlogInfo(models.Model):
    blimg=models.ImageField(upload_to='static/')
    bldate=models.CharField(max_length=20)
    bltext=models.CharField(max_length=300)
    blhead=models.CharField(max_length=100)