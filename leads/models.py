from django.db import models

# Create your models here.
class Lead(models.Model):
    SOURCE_CHOICES  = (
        ('Youtube','Youtube'),
        ('Google','Google')
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)