from django.db import models
from django.conf import settings
from api.models import Student
# Create your models here.



class Forum(models.Model):
  students = models.ManyToManyField(Student, related_name="groupchat")
  title = models.CharField(max_length=150, null=True)
  

  def __str__(self):
    return self.title
  
class Post(models.Model):
  student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True
      )
  title = models.CharField(max_length=80, null=True)
  body = models.CharField(max_length=500, null=True)
  likes = models.IntegerField(default=0)
  forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        null=True
      )
  
  
  def __str__(self):
    return f"\"{self.title}\" written by {self.student.student.username} with {self.likes} likes"

