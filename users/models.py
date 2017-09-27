"""
Model class UserInfo which extends the User model class.

"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User




class Profile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile",primary_key=True)
    firstname=models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    pic_url = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.firstname

