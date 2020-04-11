from django.db import models
from django.urls import reverse

# Create your models here.
CLEANSE =(
    ('S', 'SUNLIGHT'),
    ('D', 'MOONLIGHT'),
    ('H','HELD')
)

class Energy(models.Model):
    wellness = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    

    def __str__(self):
        return f"harnesses {self.wellness}properties, and means {self.meaning}"

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    energys = models.ManyToManyField(Energy)
   
 
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

    class Meta:
        ordering = ['-date']    
