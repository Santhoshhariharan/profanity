from django.db import models
import os
from django.conf import settings
from django.core.files import File


# Create your models here.
class profanity(models.Model):
    name = models.CharField(max_length=50,default='')
    comment = models.CharField(max_length=50,default='')

