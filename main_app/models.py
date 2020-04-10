from django.db import models

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    properties = models.TextField(max_length=250)
    meaning = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    