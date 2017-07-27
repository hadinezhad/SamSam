from django.db import models
from manageUser.models import Account
# Create your models here.


class Activity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)


class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sender')
    receiver = models.ForeignKey(Account, related_name='receiver')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    trackingCode = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Debt(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)  # TODO
    date = models.DateTimeField(auto_now=True)


class Building(models.Model):
    manager = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    info = models.TextField()


class News(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()


class Poll(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    text = models.TextField()


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        unique_together = (("poll", "id"), )


class Participate(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("poll", "vote"), )


class Unit(models.Model):
    size = models.IntegerField()
    info = models.TextField()
    id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("id", "building"),)


class Role(models.Model):
    role = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    wage = models.IntegerField()
    info = models.TextField()

    class Meta:
        unique_together = (("role", "building"),)


# TODO for plan reserved plan
class Plan(models.Model):
    pass
