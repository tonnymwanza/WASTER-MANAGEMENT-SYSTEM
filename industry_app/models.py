from django.db import models

# Create your models here.

class Waste(models.Model):
    waste_sources = models.CharField(max_length=50)
    waste_collection = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    waste_separation = models.CharField(max_length=50)
    waste_treatment = models.CharField(max_length=50)
    waste_disposal = models.CharField(max_length=50)