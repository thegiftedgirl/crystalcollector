from django.db import models
from django.urls import reverse

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    properties = models.TextField(max_length=250)
    meaning = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'crystal_id': self.id })