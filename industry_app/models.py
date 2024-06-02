from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50, null=True)
    waste_sources = models.CharField(max_length=50)
    waste_collection = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    waste_separation = models.CharField(max_length=50)
    waste_treatment = models.CharField(max_length=50)
    waste_disposal = models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()