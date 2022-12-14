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

  
  

def ??????_????????????_????????????_????????????_????????????_???????????????_???_???????????????_????????????????????????(request):
  
  data = {"result":"?????? ???????????????"}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)