from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum
from django.db.models.signals import post_save
from django.dispatch import receiver

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


@receiver(post_save, sender=User) #TODO for other users
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, type=UserType.MANAGER)

    instance.account.save()



