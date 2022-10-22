import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('sig.csv') as f:
    f.decode("cp949").encode("utf-8")
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list

print(columns['SIG_KOR_NM'])
