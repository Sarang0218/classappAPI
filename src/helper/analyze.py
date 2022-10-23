import csv
from collections import defaultdict
import requests
def setup():
  columns = defaultdict(list) # each value in each column is appended to a list
  
  with open('sig2.csv') as f:
      reader = csv.DictReader(f) # read rows into a dictionary format
      for row in reader: # read a row as {column1: value1, column2: value2,...}
          for (k,v) in row.items(): # go over each column name and value 
              columns[k].append(v) # append the value into the appropriate list
  
  
  with open("dat.txt", "r") as dat:
    txt = dat.read()
    dict = {}
    lines = txt.split("\n")
    for line in lines:
      
      toks = line.split(" | ")
      dict[toks[0]] = toks[1]
  
  bgCOUNTY = []
  specifics = []
  krc = {}
  for i in range(len(columns['SIG_KOR_NM'])):
    bgCOUNTY.append(dict[columns["SIG_CD"][i][:2]])
    specifics.append(columns['SIG_KOR_NM'][i])
    krc[columns['SIG_KOR_NM'][i]] = dict[columns["SIG_CD"][i][:2]]
    
    
  return {"KRC" : krc, "BGCOUNTY" : bgCOUNTY, "SPECIFICS": specifics}


def get_states():
  mylist = setup()["BGCOUNTY"]
  mylist = list(dict.fromkeys(mylist))
  
  return mylist

def get_locals(state):
  listR = []
  krc = setup()["KRC"]
  for item in krc:
    if krc[item] == state:
      listR.append(item)
  return listR

def getCozima(state):
  with open("ck.txt", "r") as dat:
    txt = dat.read()
    dict = {}
    lines = txt.split("\n")
    for line in lines:
      
      toks = line.split(" : ")
      dict[toks[0]] = toks[1]
  return dict[state]
def get_school(state, local, schlTYPE):
  code = getCozima(state)
  datac = requests.get(f"https://open.neis.go.kr/hub/schoolInfo?KEY=2d4128bc16f24606b365a2a664d4620d&Type=json&pIndex=1&pSize=1000&ATPT_OFCDC_SC_CODE={code}&SCHUL_KND_SC_NM={schlTYPE}").json()
  print("saver")
  list = []
  locSCHL = datac["schoolInfo"][1]["row"]
  for item in locSCHL:
    if local in item["ORG_RDNMA"]:
      print(item["SCHUL_NM"])
      print(item["SD_SCHUL_CODE"])
      list.append({item["SCHUL_NM"]:item["SD_SCHUL_CODE"]})
         
  return list
    
    





#오 천재