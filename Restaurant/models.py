from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phoneNumber = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='restaurants', blank=True)
    pictures = models.ImageField(upload_to='restaurants', blank=True, null=True)
    CUISINE_CHOICES = [
        ('american', 'American'),
        ('chinese', 'Chinese'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('indian', 'Indian'),
    ]
    
    # Define the cuisine field
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES, default='chinese')
    menu = models.TextField(blank=True, null=True)

 
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()



    def __str__(self):
        return self.name

    
# Create your models here.
