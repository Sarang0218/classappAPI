import requests

# https://classappapi.compilingcoder.repl.co/forum/query/1/

response = requests.post("https://classappapi.compilingcoder.repl.co/forum/send/1/9", {"title":"Helpme","body":"oksick"})
print(response.json())