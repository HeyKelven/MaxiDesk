import tools, csv
from tkinter import *
from win32api import GetSystemMetrics

def down(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1000,height=300)

root = Tk()
root.title('MaxiDesk')
root.geometry('1000x300+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))
root.resizable(False, False)

principal_frame = Frame(root).pack(fill=BOTH)

canvas = Canvas(principal_frame)
second_frame = Frame(canvas, height=10)

data = []
with open(tools.path_vendas, 'r') as looking_at:
    reader = csv.reader(looking_at)
    title = []
    i = 0
    for row in reader:
        data.append(row)
        if row[4] == "0":
            person = Label(second_frame, text='Solicitante: ' + row[0]).grid(row=i, column=0, sticky=W, padx=(15,15))
            dpto = Label(second_frame, text='Departamento: ' + row[1]).grid(row=i, column=1, sticky=W, padx=(15,15))
            problem = Label(second_frame, text='Problema: ' + row[2]).grid(row=i, column=2, sticky=W, padx=(15,15))
            opening_date = Label(second_frame, text='Data de abertura: ' + row[6] + ' ' + row[5]).grid(row=i, column=3, sticky=W, padx=(15,15))
            num_id = Label(second_frame, text='Id: ' + row[3]).grid(row=i, column=4, sticky=W, padx=(15,15))
            i += 1

scroll = Scrollbar(principal_frame, orient='vertical', command = canvas.yview)
canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side='right', fill=Y)
canvas.pack()
canvas.create_window((0,0),window=second_frame)

second_frame.bind('<Configure>',down)

root.mainloop()


