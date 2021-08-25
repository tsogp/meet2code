from django.db import models
from django.contrib.auth.models import Group, Permission, models
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30, unique=True)


