import datetime
from django.contrib.auth.models import User
from django.db import models


import uuid
from django.db import models





class Offer(models.Model):
    image = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=1000,blank=True)
    brand=models.CharField(max_length=1000,blank=True)
    price = models.CharField(max_length=1000, blank=True)
    detail = models.CharField(max_length=1000,blank=True)
    redeem = models.CharField(max_length=1000,blank=True)
    percent=models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    def __unicode__(self):
        return self.title

class Transaction(models.Model):
    user=models.ForeignKey(User)
    tr_id = models.CharField(max_length=12,blank=True)
    amount = models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    item = models.CharField(max_length=1000,blank=True)
    reward = models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    tr_date=models.DateField(default=datetime.date.today, blank=True)

    def __unicode__(self):
        return self.item+" "+str(self.user.first_name)

class Wallet(models.Model):
    user=models.ForeignKey(User,primary_key=True)
    amount = models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    treward = models.DecimalField(max_digits=15,decimal_places=2,blank=True)
    def __unicode__(self):
        return str(self.user.first_name)
class Card(models.Model):
    user=models.ForeignKey(User,primary_key=True)
    cardnumber = models.CharField(max_length=16,blank=True)
    expiry_month = models.CharField(max_length=2,blank=True)
    expiry_year = models.CharField(max_length=4,blank=True)
    cvv = models.CharField(max_length=3,blank=True)
    card_type = models.CharField(max_length=20,blank=True)
    def __unicode__(self):
        return str(self.user.first_name)+self.card_type

class ShopCart(models.Model):
    user=models.ForeignKey(User)
    item=models.ForeignKey(Offer)

    def __unicode__(self):
        return str(self.user.first_name)+" "+str(self.item.title)