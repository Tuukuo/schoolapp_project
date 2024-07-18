from django.db import models

# Create your models here.

class Lecture(models.Model):
  class_name=models.CharField(max_length=20) 
  class_size=models.PositiveSmallIntegerField()
  number_of_students=models.PositiveSmallIntegerField()
  section = models.CharField(max_length=20)
  
def __str__(self):
  return f"{self.class_name} {self.class_size}"




   





