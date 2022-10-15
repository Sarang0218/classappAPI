# Sirius Student Management API
## 시리우스의 종합 학생 관리 시스템
### 개발 현황:
- [X] 시간표 API
- [X] 급식 API
- [x] Todo API
- [ ] Chat API
- [ ] 회원 Customization API





# 시간표 API
### 시간표 불러오기 <br>
TYPE: **GET REQUEST**
```json

 
{ "timesc" : 
  [
    {
        "title" : "영어",
        "period" : 1
    },
    {
        "title" : "국어",
        "period" : 2
    },
  ]
}

```

URL/timesc/studentPk/시간표일자(YYYYMMDD)/<br>
[예시](https://classappAPI.compilingcoder.repl.co/api/timesc/B10/7021137/2022/20220610/1/1/8)

# User API
### 유저 생성 <br>
TYPE: **POST REQUEST**

```json
{
  "result":"success",
  "pk":1
}
```
#### 에러 예시
```json
{
  "result":"fail",
  "reason":"Already Existing ID"
}
```
전달값<br>
"username"
"password"

URL/signup/stclasstype/edumintype/grade

### 로그인 (로그체크) <br>

```json
{
  "result":"success",
}
```

전달값<br>
"username"
"password"


URL/api/logcheck
# To do list API

### Todo 생성
TYPE: **GET REQUEST**
```json
{
  "result":"success",
  "todopk":2
}
```
URL/todoList/create/StudentPk/title/body/<br>

### Todo 보기
TYPE: **GET REQUEST**

```json
{
   "todo":[
      {
        "title":"수학의 정석 수(하) 풀기",
        "body":"p27~p33",
        "subject":"수학",
        "todopk":2
      }
   ]
}
```

### Todo 삭제
TYPE: **GET REQUEST**
```json
{
  "result":"success",
}
```
URL/todoList/delete/todoPk/<br>

# Chat API (Not Implemented)
## 메세지 보내기
TYPE: **GET REQUEST**
```json
{
  "result":"success"
}
```
URL/chat/send/messageTxt/studentPk/GroupchatPk<br>
## 메세지 모두 불러오기
```json
{
   "messages":[
      {
        "message":"ㅋㅋㅋ 나 이번에 전교 1등임",
        "studentPk":1,
        "groupChatPk":12
      },
      {
        "message":"응 어쩔티비",
        "studentPk":2,
        "groupChatPk":12
      }
   ]
}
  ```
URL/api/chat/get/GroupchatPk

#  급식 API
### 시간표 불러오기 <br>
TYPE: **GET REQUEST**
```json
{
    "food":{
        "menu":[
            "후리카케밥  (2.5.6.10.13.)",
            "미트스파게티.  (1.2.5.6.10.12.13.16.18.)",
            "포기김치.  (9.13.)",
            "음료  (5.13.)",
            "불고기치아바타샌드위치  (1.2.5.6.12.13.16.)",
            "모듬피클.  (13.)",
            "열대과일샐러드  (1.5.13.)"
        ]
    }
}
```
URL/food/StudentPk/시간표일자(YYYYMMDD)/<br>
[예시](https://classappapi.compilingcoder.repl.co/api/food/B10/7021137/20220610/)


