from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum
# Create your models here.


class UserType(IntEnum):
    MANAGER = 1
    NEIGHBOR = 2
    PERSONNEL = 3


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(default=UserType.MANAGER)

    def __str__(self):
        return self.user.first_name





