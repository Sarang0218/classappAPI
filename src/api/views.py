from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
import os
import json
import requests
from .models import Student, Todo, GroupChat, Message
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import Crypto
from Crypto.publickey import RSA
from Crypto import Random


## HELPERS ##
def rDatStat(res, reason):
  data = {"result":res, "reason":reason}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
        ds,
        content_type=u"application/json; charset=utf-8",
        status=200)


#급식#
#시간표/급식#
def getData(request, pk, year, ymd, sem):
  print(os.getenv("KEY"))
  s = Student.object.get(pk=pk)
  
  datac = requests.get(f"https://open.neis.go.kr/hub/misTimetable?KEY=2d4128bc16f24606b365a2a664d4620d&Type=json&pIndex=1&ATPT_OFCDC_SC_CODE={s.edumintype}&SD_SCHUL_CODE={s.school}&AY={year}&ALL_TI_YMD={ymd}&GRADE={s.grade}&SEM={sem}&CLASS_NM={s.stclasstype}").json() 
  
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

def getDatalunc(request, pk, sc, ymd):
  print(os.getenv("KEY"))
  s = Student.objects.get(pk=pk)
  
  datac = requests.get(f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=fc1214b4b3844ebe865233e7cf37f20d&Type=json&pIndex=1&pSize=10&ATPT_OFCDC_SC_CODE={s.edumintype}&SD_SCHUL_CODE={sc}&MLSV_YMD={ymd}").json() 
  alld = []
  for item in datac["mealServiceDietInfo"][1]["row"]:
    print(item)
    send_data = {"menu":item["DDISH_NM"].split("<br/>")}
    alld = send_data
  data = {"food":alld}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)

#회원#
#회원#
@csrf_exempt
def signUpUser(request, stclasstype, edumintype,  grade, school):
    #User 모델에 객체 생성
    # stu에 대입
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    try:
      user = User.objects.create_user(username, password=password)
      user.save()
      stu = Student.objects.create(student = user, stclasstype =  stclasstype, edumintype = edumintype,  grade = grade, school=school)
    except IntegrityError:
      data = {"result":"fail", "reason":"Already Existing ID"}
      ds = json.dumps(data, ensure_ascii=False)
      return rDatStat(res="fail", reason="Already Existing ID")
    

  
  user.save()
  stu.save()

  #성공
  data = {"result":"success", "pk":stu.pk}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
@csrf_exempt
def logcheck(request):
  user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
  if user is not None:
      return rDatStat(res="Success", reason="Succeeded in authentication")  
  else:
      return rDatStat(res="fail", reason="invalid data")

#RSAenctypt
def pkencrypt(request, pk):
  
#TODOs#
def todoCreate(request, pk, title, body, subject):
  try:
    stu = Student.objects.get(pk=pk)
    td = Todo.objects.create(student=stu, todoTitle=title, todoBody=body, subject=subject)
    data = {"result":"success","todopk":td.pk}
    td.save()
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
      send_data = {"title":item.todoTitle, "body":item.todoBody, "subject":item.subject, "todopk":item.pk}
      
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

def todoDel(request, todoPk):
  try:
    todo = Todo.objects.get(pk=todoPk)
    todo.delete()
    data = {"result":"success"}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=200)
  except:
    data = {"result":"fail", "reason":"Failed during query."}
    ds = json.dumps(data, ensure_ascii=False)
    return HttpResponse(
      ds,
      content_type=u"application/json; charset=utf-8",
      status=500)



  
  
    

    
  
  
