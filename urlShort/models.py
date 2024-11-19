from django.db import models

# Create your models here.

class Urls(models.Model):
    url = models.CharField(max_length=122)
    decoded = models.CharField(max_length=122)

