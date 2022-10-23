# 완 료 ! ! ! ! ! !   가즈아아아아아아

# Sirius Student Management API


## 시리우스의 종합 학생 관리 시스템
### 개발 현황:
- [X] 시간표 API
- [X] 급식 API
- [x] Todo API
- [x] 조회 API
- [X] 게시판 API






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
[예시](https://classappAPI.compilingcoder.repl.co/timesc/1/20221013)

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

URL/signup/stclasstype/school/edumintype/grade

### 로그인 (로그체크) <br>

```json
{
  "result":"success",
  "res":"Succeeded in <AREA>",
  "pk":777
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

# 게시판 API 
## 글 쓰기
TYPE: **GET REQUEST**
```json
{
  "result":"SUCCESS!!!"
}
```
전달값<br>
"title"
"body"

URL/forum/send/<forumpk\>/<studentpk\><br>
## 글 조회
```json
{
   "result":[
      {
         "title":"히히",
         "body":"크크루삥뽕",
         "likes":3,
         "author":"tte",
         "id":1
      },
      {
         "title":"OOOOOO",
         "body":"oksick",
         "likes":1,
         "author":"tt7",
         "id":2
      },
      {
         "title":"Helpme",
         "body":"oksick",
         "likes":0,
         "author":"tt7",
         "id":3
      }
   ]
}
  ```
URL/forum/query/<forumpk\><br>

## 좋아요
```json
{
  "result":"SUCCESS!!!"
}
```

URL/forum/like/<postid\>

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
[예시](https://classappapi.compilingcoder.repl.co/food/1/20221013/)

# 조회 API

### Local Group 모두 불러오기 (시도)
URL/getlocals

### Galaxy 모두 불러오기 (좀 더 세부적인거...)
URL/getgalaxies/[시도]

### 학교 불러오기
URL/getschool/[시도]/[구/시]/[학교 종류: 중학교, 고등학교, 등]