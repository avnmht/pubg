from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=100)
class mainform(models.Model):
    Username=models.CharField(max_length=200)
    fullname=models.CharField(max_length=12, unique=True)
    ingamename=models.CharField(max_length=200, unique=True)
    region=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    characterid=models.CharField(max_length=200, unique=True)
    kperd=models.CharField(max_length=200)
    yourtier=models.CharField(max_length=200)
    gameserver=models.CharField(max_length=200)
    winpermatches=models.CharField(max_length=200)
    tpporfpp=models.CharField(max_length=200)
    insquad=models.CharField(max_length=200)