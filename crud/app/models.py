from django.db import models

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    fess = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return self.subject

state=(('dhar','dhar'),
       ('ujjain','ujjain'),
       ('bhopal','bhopal'),
       )
class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,choices=state)
    mobile = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stud/')

