from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os
import json
import requests
from .models import Student, Todo
from django.contrib.auth.models import User
# Create your views here.
from django.db import IntegrityError


def getData(request, sido, sc, year, ymd, sem, rn, grade):
  print(os.getenv("KEY"))
  
  
  datac = requests.get(f"https://open.neis.go.kr/hub/misTimetable?KEY=2d4128bc16f24606b365a2a664d4620d&Type=json&pIndex=1&ATPT_OFCDC_SC_CODE={sido}&SD_SCHUL_CODE={sc}&AY={year}&ALL_TI_YMD={ymd}&GRADE={1}&SEM={sem}&CLASS_NM={rn}").json() 
  
  i = 0
  alld = []
  for item in datac["misTimetable"][1]["row"]:
    i+=1
    send_data = {"title":item["ITRT_CNTNT"][1:], "period":i}
    
    alld.append(send_data)
    print(alld)

  data = {"timesc":alld}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)


def signUpUser(request, username,password, stclasstype, edumintype,  grade):
    #User 모델에 객체 생성
    # stu에 대입
  try:
    user = User.objects.create_user(username, password=password)
    user.save()
    stu = Student.objects.create(student = user, stclasstype =  stclasstype, edumintype = edumintype,  grade = grade)
  except IntegrityError:
    data = {"result":"fail", "reason":"Already Existing ID"}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
    

  
  user.save()
  stu.save()

  #성공
  data = {"result":"success", "pk":stu.pk}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
  

  

  
  
  
  
def todoCreate(request, pk, title, body):
  try:
    stu = Student.objects.get(pk=pk)
    Todo.objects.create(student=stu, todoTitle=title, todoBody=body)
    data = {"result":"success"}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)
  except:
    data = {"result":"fail"}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)

def todoGet(request, pk):
  try:
    stu = Student.objects.get(pk=pk)
    todos = Todo.objects.filter(student=stu)
    # 나중에 ㅋ
    i = 0
    alld = []
    for item in todos:
      i+=1
      send_data = {"title":item.todoTitle, "body":item.todoBody}
      
      alld.append(send_data)
      print(alld)
  
    data = {"todo":alld}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)
      
      

  except:
    #zz
    pass
    

    
  
  
