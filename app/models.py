from django.db import models

# Create your models here.

class Userform(models.Model):
    From = models.EmailField(max_length=100)
    To = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=250)