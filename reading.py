import csv, tools
import os.path, time

data = []
with open (tools.path_vendas, 'r') as looking_at:
    reader = csv.reader(looking_at)
    for row in reader:
        data.append(row)
        if row[4] == "0":
            print(row)

tempo = time.ctime(os.path.getmtime(tools.path_vendas))

with open (tools.path_vendas, 'r') as looking_at:
    reader = csv.reader(looking_at)
    while 1:
        if time.ctime(os.path.getmtime(tools.path_vendas)) != tempo:
            tempo = time.ctime(os.path.getmtime(tools.path_vendas))
            for row in reader:
                if row not in data:
                    print(row)
                    data.append(row)