from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    control_number = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)