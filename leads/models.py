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

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    '''phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)'''

    #FOREIGN KEY ISSUES

class Agent(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
