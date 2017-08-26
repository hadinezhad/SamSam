from django.db import models
from manageUser.models import Account
from django.utils import timezone
# Create your models here.


class Activity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100)


class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sender')
    receiver = models.ForeignKey(Account, related_name='receiver')
    subject = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class Debt(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    date = models.DateTimeField()


class Building(models.Model):
    manager = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    info = models.TextField()

    def __str__(self):
        return self.name + " " + self.manager.user.first_name + " " + self.manager.user.last_name


class Transaction(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    trackingCode = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


class FailureReport(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()
    subject = models.CharField(max_length=100)


class News(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()
    subject = models.CharField(max_length=100)


class Poll(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    text = models.TextField()
    subject = models.CharField(max_length=100)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()
    number = models.IntegerField()


class Participate(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Unit(models.Model):
    size = models.IntegerField()
    info = models.TextField()
    number = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.building.name + " " + self.account.user.first_name + " " + self.account.user.last_name


class Role(models.Model):
    role = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    wage = models.IntegerField()
    info = models.TextField()


class Feature(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return self.title + " " + self.startDate.__str__()


class ReservedFeature(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    reservedDate = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


