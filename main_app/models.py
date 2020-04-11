from django.db import models
from django.urls import reverse

# Create your models here.
CLEANSE =(
    ('H','HELD'),
    ('S', 'SUNLIGHT'),
    ('D', 'MOONLIGHT')
)

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

class Cleansing(models.Model):
    date = models.DateField('cleansing date')
    cleanse = models.CharField(
        max_length=1,
            choices=CLEANSE,
            default=CLEANSE[0][0]
    )
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_cleanse_display()} on {self.date}"
