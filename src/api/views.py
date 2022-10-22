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
from helper import analyze

## HELPERS ##
def rDatStat(res, reason, pk=None):
  data = {"result":res, "reason":reason}
  if pk:
    data["pk"] = pk
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
        ds,
        content_type=u"application/json; charset=utf-8",
        status=200)


#급식#
#시간표/급식#
def getData(request, pk, ymd):
  try:
    print(os.getenv("KEY"))
    try: 
      s = Student.objects.get(pk=pk);
    except Exception as e: 
      return rDatStat("강지오 바보 ERROR", str(e))
    
    #https://open.neis.go.kr/hub/misTimetable?KEY=2d4128bc16f24606b365a2a664d4620d&Type=json&pIndex=1&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7021137&AY=2022&ALL_TI_YMD=20220610&GRADE=1&SEM=1&CLASS_NM=1
    datac = requests.get(f"https://open.neis.go.kr/hub/misTimetable?KEY=2d4128bc16f24606b365a2a664d4620d&Type=json&pIndex=1&ATPT_OFCDC_SC_CODE={s.edumintype}&SD_SCHUL_CODE={s.school}&ALL_TI_YMD={ymd}&GRADE={s.grade}&CLASS_NM={s.stclasstype}").json() 
  
    
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
  except Exception as e:
    return rDatStat("박사랑 바보 ERROR", str(e))

def getDatalunc(request, pk, ymd):
  print(os.getenv("KEY"))
  
  s = Student.objects.get(pk=pk)
  
  datac = requests.get(f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=fc1214b4b3844ebe865233e7cf37f20d&Type=json&pIndex=1&pSize=10&ATPT_OFCDC_SC_CODE={s.edumintype}&SD_SCHUL_CODE={s.school}&MLSV_YMD={ymd}").json() 
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
  print(request.POST)
  try:
    if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
  
    
    try:
        user = User.objects.create_user(username, password=password)
        user.save()
        stu = Student.objects.create(student = user, stclasstype =  stclasstype, edumintype = edumintype,  grade = grade, school=school)
        stu.save()
    except Exception as e:
        data = {"result":"fail", "reason":str(e)}
        ds = json.dumps(data, ensure_ascii=False)
        return rDatStat(res="fail", reason=str(e))
  except KeyboardInterrupt as ks:
    print(request.POST)
    
    return rDatStat(res="failY", reason = str(ks))
    
  
  
  

  #성공
  data = {"result":"success", "pk":stu.pk}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
def signUpUserGet(request, stclasstype, edumintype,  grade, school, user, pw):
    #User 모델에 객체 생성
    # stu에 대입
  try:
    
    username = user
    password = pw
    try:
        user = User.objects.create_user(username, password=password)
        user.save()
        stu = Student.objects.create(student = user, stclasstype =  stclasstype, edumintype = edumintype,  grade = grade, school=school)
        stu.save()
    except Exception as e:
        data = {"result":"fail", "reason":str(e)}
        ds = json.dumps(data, ensure_ascii=False)
        return rDatStat(res="fail", reason=str(e))
  except KeyboardInterrupt as ks:  
    return rDatStat(res="failY", reason = str(ks))
  #성공
  data = {"result":"success", "pk":stu.pk}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
@csrf_exempt
def logcheck(request):
  user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
  if user is not None:
      stu = Student.objects.get(student=user)
      return rDatStat(res="Success", reason="Succeeded in authentication", pk=stu.pk)  
  else:
      return rDatStat(res="fail", reason="invalid data")



def logcheckGet(request, user, password):
  user = authenticate(request, username=user, password=password)
  if user is not None:
      stu = Student.objects.get(student=user)
      return rDatStat(res="Success", reason="Succeeded in authentication", pk=stu.pk)  
  else:
      return rDatStat(res="fail", reason="invalid data")

def getLocalGroups(request):
  states = list(analyze.get_states())
  data = {"result":"success", "locals":states}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
def getGalax(request,state):
  galax = analyze.get_locals(state)
  data = {"result":"success", "galaxies":galax}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)

def getSys(request, state, local, schltype):
  schools = analyze.get_school(state, local, schltype)
  data = {"result":"success", "schools":schools}
  ds = json.dumps(data, ensure_ascii=False)
  return HttpResponse(
    ds,
    content_type=u"application/json; charset=utf-8",
    status=200)
#RSAenctypt
def pkencrypt(request, pk):
  #        
  
  pass
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



  
  
    

    
  
  
