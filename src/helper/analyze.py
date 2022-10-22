import csv
from collections import defaultdict

def setup():
  columns = defaultdict(list) # each value in each column is appended to a list
  
  with open('sig2.csv') as f:
      reader = csv.DictReader(f) # read rows into a dictionary format
      for row in reader: # read a row as {column1: value1, column2: value2,...}
          for (k,v) in row.items(): # go over each column name and value 
              columns[k].append(v) # append the value into the appropriate list
  
  #print(columns['SIG_KOR_NM'])
  
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
  return set(setup()["BGCOUNTY"])

def get_locals(state):
  listR = []
  krc = setup()["KRC"]
  for item in krc:
    if krc[item] == state:
      listR.append(item)
  return listR

print(get_locals("부산시"))





#오 천재