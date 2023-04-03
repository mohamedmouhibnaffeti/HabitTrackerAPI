from django.db import models
# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)

class Task(models.Model):
    owner = models.CharField(max_length=30, default="")
    name = models.CharField(max_length=50,default="")
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
