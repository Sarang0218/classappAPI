# API
## 시간표 API
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

## User API

```json
{
  "result":"success",
  "pk":1
}
```
### 에러 예시
```json
{
  "result":"fail",
  "reason":"Already Existing ID"
}
```
URL/api/signup/username/password/stclasstype/edumintype/grade

## To do list API

### Todo 생성
```json
{
  "result":"success",
}
```
URL/api/todoList/create/StudentPk/title/body/<br>

### Todo 보기

```json
{
   "todo":[
      {
         "title":"수학의 정석 수(하) 풀기",
         "body":"p27~p33"
      }
   ]
}
```

URL/api/todoList/view/StudentPk/<br>


URL/api/todoList/delete/StudentPk//<br>
```json

```
