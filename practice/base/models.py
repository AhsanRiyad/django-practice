from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class MyModel(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


