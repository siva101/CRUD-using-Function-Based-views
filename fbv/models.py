from django.db import models

class Student(models.Model):
    Fname=models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Score = models.FloatField()



# Create your models here.
