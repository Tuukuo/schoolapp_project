from django.db import models

# Create your models here.

class Lecture(models.Model):
  class_name=models.CharField(max_length=20) 
  class_size=models.PositiveSmallIntegerField()
  number_of_students=models.PositiveSmallIntegerField()
  section = models.CharField(max_length=20)
  teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,related_name='courses')
  students = models.ManyToManyField(Students)
  Course= models.ForeignKey(Course,on_delete=models.CASCADE)
  

def __str__(self):
  return f"{self.class_name} {self.class_size}"




   





