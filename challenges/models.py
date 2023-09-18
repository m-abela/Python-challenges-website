from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    answer = models.CharField(max_length=100)
