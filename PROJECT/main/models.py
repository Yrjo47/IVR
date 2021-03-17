from django.db import models
import datetime
from time import sleep

from django.contrib.auth.models import User


# Create your models here.

class Clock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    settedtime = models.DateTimeField()
    isactive = models.BooleanField(default=False)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title


