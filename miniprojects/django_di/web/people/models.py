from django.db import models

__all__ = ['Person']


class Person(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
