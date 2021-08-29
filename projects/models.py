from django.db import models
from django.contrib.auth.models import Group, Permission, models
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey('Owner', related_name='Project')
    bio = models.CharField(max_length=1500)

    current_amount = models.IntegerField(default=1)
    max_amount = models.IntegerField(default=4)





