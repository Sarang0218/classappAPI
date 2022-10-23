from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):
  student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
  )
  school = models.CharField(max_length=30, null=True)
  grade = models.IntegerField()
  stclasstype = models.IntegerField(null=True)
  edumintype = models.CharField(max_length=30, null=True)


  def __str__(self):
    return self.student.username

class Todo(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True
      )
    
    todoTitle = models.CharField(max_length=150, null=True)
    todoBody = models.CharField(max_length=300, null=True)
    subject = models.CharField(max_length=15, null=True) 

    def __str__(self):
      return self.todoTitle
