import tools, csv
from tkinter import *
from win32api import GetSystemMetrics

root = Tk()
root.title('MaxiDesk')
root.geometry('1000x300+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))

data = []
with open (tools.path_vendas, 'r') as looking_at:
    reader = csv.reader(looking_at)
    title = []
    i = 0
    for row in reader:
        data.append(row)
        if row[4] == "0":
            person = Label(root, text= 'Solicitante: ' + row[0]).grid(row=i, column=0, sticky=W, padx=(15,15))
            dpto = Label(root, text= 'Departamento: ' + row[1]).grid(row=i, column=1, sticky=W, padx=(15,15))
            problem = Label(root, text= 'Problema: ' + row[2]).grid(row=i, column=2, sticky=W, padx=(15,15))
            opening_date = Label(root, text= 'Data de abertura: ' + row[6] + ' ' + row[5]).grid(row=i, column=3, sticky=W, padx=(15,15))
            num_id = Label(root, text= 'Id: ' + row[3]).grid(row=i, column=4, sticky=W, padx=(15,15))
            i += 1

root.mainloop()
