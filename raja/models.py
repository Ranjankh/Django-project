

from django.db import models
# create your model here

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length = 100)
    age = models.IntegerField()


    def __str__(self)->str: 
        return f"{self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    Subjectname = models.CharField(max_length=100)
    periods = models.IntegerField()

    def __str__(self)->str: 
        return f"{self.name}"


