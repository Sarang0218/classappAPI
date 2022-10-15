import requests

response = requests.post("https://classappAPI.compilingcoder.repl.co/api/signup/8/7021137/B10/1", {"username":"인생참뭐없다ㅋㅋ아이고ㄹㅇㅋㅋ", "password":"ㅅㅂ..."})
print(response.json())
