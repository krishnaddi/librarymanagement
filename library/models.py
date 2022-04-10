from django.db import models

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=32)
    author=models.CharField(max_length=32)
    price=models.IntegerField()
    