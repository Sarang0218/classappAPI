# Sirius Student Management API
## 시리우스의 종합 학생 관리 시스템
### 개발 현황:
- [X] 시간표 API
- [ ] 급식 API
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

URL/api/timesc/시도교육청코드/표준학교코드/학년도/시간표일자(YYYYMMDD)/학기/학년/반번호<br>
[예시](https://classappAPI.compilingcoder.repl.co/api/timesc/B10/7021137/2022/20220610/1/1/8)

# User API
### 유저 생성 <br>
TYPE: **GET REQUEST**

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
URL/api/signup/username/password/stclasstype/edumintype/grade

# To do list API

### Todo 생성
TYPE: **GET REQUEST**
```json
{
  "result":"success",
  "todopk":2
}
```
URL/api/todoList/create/StudentPk/title/body/<br>

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
URL/api/todoList/delete/todoPk/<br>

# Chat API (Not Implemented)
## 메세지 보내기
TYPE: **GET REQUEST**
```json
{
  "result":"success"
}
```
URL/api/chat/send/messageTxt/studentPk/GroupchatPk<br>
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