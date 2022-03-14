from asyncio.windows_events import NULL
from operator import mod
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
from django.db import models

class Colleges(models.Model):
    Name = models.CharField(max_length= 1000)
    ScholarshipName = models.CharField(max_length= 1000, null=True)
    MinimumSAT = models.IntegerField(blank=True,null=True)
    MinimumGpa = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    Informationlink = models.URLField(null=True)
    Collegwebsite = models.URLField(null=True)
    Deadlines = models.CharField(max_length= 1000,null=True)
    CommanApp = models.CharField(max_length= 1000,null=True)
    Wes = models.CharField(max_length= 1000,null=True)
    Additionalinformation = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.Name



class Interview(models.Model):
    Name = models.CharField(max_length=100)
    Content = models.TextField(validators=[MinLengthValidator(10)],null=True)
    def __str__(self):
        return self.Name
