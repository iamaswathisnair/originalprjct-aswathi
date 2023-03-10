from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    start_date =  models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(auto_now=True)
    completionstatus = models.TextField(max_length=255)
    description = models.TextField(max_length=400)
    userid = models.IntegerField(max_length=50)

class Category(models.Model):
    all =  models.CharField(max_length=400)
    work =  models.CharField(max_length=400)
    personal =  models.CharField(max_length=400)
    whishlist =  models.CharField(max_length=400)
    birthday =  models.CharField(max_length=400)
    habits =  models.CharField(max_length=400)
    learing =  models.CharField(max_length=400)
