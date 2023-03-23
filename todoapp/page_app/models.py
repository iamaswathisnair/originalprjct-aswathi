from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    CHOICES = (
    ("ADMIN", "ADMIN"),
    ("USER", "USER")
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    type = models.CharField(max_length=150, choices = CHOICES, default ='USER')

class Task(models.Model):
    title = models.CharField(max_length=50)
    start_date =  models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(auto_now=True)
    completionstatus = models.TextField(max_length=255)
    description = models.TextField(max_length=400)
    userid = models.IntegerField(max_length=50)

class Category(models.Model):
    CHOICES = (
    ("ALL", "ALL"),
    ("WORK", "WORK"),
    ("PERSONAL", "PERSONAL"),
    ("WHISLIST", "WHISLIST"),
    ("BIRTHDAY", "BIRTHDAY"),
    ("HABITS", "HABITS"),
    ("LEARNING", "LEARNING")

    )
    name =  models.CharField(max_length=400, choices = CHOICES, default ='ALL') 


