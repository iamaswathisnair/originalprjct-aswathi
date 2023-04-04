from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Profile(models.Model):
    CHOICES = (
    ("ADMIN", "ADMIN"),
    ("USER", "USER")
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    type = models.CharField(max_length=150, choices = CHOICES, default ='USER')
    theme = models.CharField(max_length=150,default="orange")

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

    def __str__(self):
            return self.name

class Task(models.Model):
    CHOICES = (
    ("ON GOING", "ON GOING"),
    ("DONE", "DONE")
    
    )
    title = models.CharField(max_length=50)
    start_date =  models.DateTimeField(auto_now_add=False)
    end_date =  models.DateTimeField(auto_now=False)
    deadline = models.DateTimeField(auto_now=False)
    completionstatus = models.CharField(max_length=255,choices=CHOICES)
    description = models.TextField(max_length=400)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def is_past_due(self):
        return datetime.now().date() > self.end_date.date()


class Quotes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
