
from django.db import models

class Course(models.Model):
  course_name=models.CharField(max_length=20) 
  course_code =models.PositiveSmallIntegerField()
  teacher=models.CharField(max_length=20)
  number_of_topics=models.PositiveSmallIntegerField(null='False')
  duration_of_course= models.DateField(null='False')
  number_of_students= models.IntegerField(null='False')
  description_of_course= models.TextField(blank='False')
  fees_required= models.IntegerField(null='False')







def __str__(self):
       return f"{self.course_name} {self.course_code}"



   






