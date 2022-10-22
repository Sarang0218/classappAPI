import requests

response = requests.post("https://classappAPI.compilingcoder.repl.co/signup/8/7021137/B10/1", {"username":"testA","password":"tt"})
print(response.json())
