from django.shortcuts import render
from .models import Forum, Post
from api.models import Student
import requests
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
import os
import json
import requests


# Create your views here.
@csrf_exempt
def writePost(request, forumPk, studentPk):
  if request.POST:
    title=request.POST["title"]
    body=request.POST["body"]
    
  forum = Forum.objects.get(pk=forumPk)
  student = Student.objects.get(pk=studentPk)
  
  post = Post.objects.create(title=title, body=body, likes=0, forum=forum, student=student)

  post.save()
  data = {"result":"SUCCESS!!!!"}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)

def writePostGet(request, forumPk, studentPk, title, body):
  
    
  forum = Forum.objects.get(pk=forumPk)
  student = Student.objects.get(pk=studentPk)
  
  post = Post.objects.create(title=title, body=body, likes=0, forum=forum, student=student)

  post.save()
  data = {"result":"SUCCESS!!!!"}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)

def getPosts(request, forumPk):
  forum = Forum.objects.get(pk=forumPk)
  posts = Post.objects.filter(forum=forum)
  list = []
  
  for post in posts:
    print(post)
    list.append({"title":post.title, "body":post.body,"likes":post.likes,"author":post.student.student.username, "id":post.pk})
  data = {"result":list}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)

def like(request, postid):
    post = Post.objects.get(pk=postid)
    post.likes += 1
    post.save()
    data = {"result":"SUCCESS!!!!"}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
        ds,
        content_type=u"application/json; charset=utf-8",
        status=200)

  
  

def 씨발_어쩌다가_내인생이_이지랄이_됐는지는_모르겠지만_하_개피곤하네_씨이이이이바아알(request):
  
  data = {"result":"ㅈ까 씨발새끼야"}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)