from django.db import models

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    season = models.CharField(max_length=20, blank=False, default='')
    starts = models.CharField(max_length=20, blank=False, default='')
    ends = models.CharField(max_length=20, blank=False, default='')
    location = models.CharField(max_length=70, blank=False, default='')
    registration_open = models.BooleanField(default=False)