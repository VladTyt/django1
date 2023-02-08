from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class Table(models.Model):
    column1 = models.CharField(max_length=100)
    column2 = models.CharField(max_length=100)