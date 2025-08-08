from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

LEVELS = (
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advanced')
)

class Hobby(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hobby-detail', kwargs={'pk': self.id})
    

class Craft(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        default=LEVELS[0][0]
    )
    supplies = models.CharField(max_length=250)
    instructions = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobbies = models.ManyToManyField(Hobby)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('craft-detail', kwargs={'craft_id': self.id})