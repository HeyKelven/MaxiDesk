import tools
import csv
import time
import os.path
from tkinter import *
from tkinter import messagebox
from win32api import GetSystemMetrics
import threading

def conclude_call(id):
    archive = tools.read_csv(tools.path_vendas)
    for row in archive:
        if row[3] == id:
            print(row[1])

def put_label(frame, put_row, count):
    if put_row[4] == "0":
        v = StringVar()
        v.set("Pendente")
        Label(frame, text='Solicitante: ' + put_row[0]).grid(row=count, column=0, sticky=W, padx=(5, 10))
        Label(frame, text='Departamento: ' + put_row[2]).grid(row=count, column=1, sticky=W, padx=(0, 5))
        Label(frame, text='Problema: ' + put_row[1]).grid(row=count, column=2, sticky=W, padx=(0, 7))
        Label(frame, text='Data de abertura: ' + put_row[6] + ' ' + row[5]) \
            .grid(row=count, column=3, sticky=W, padx=(7, 7))
        Label(frame, text='Id: ' + put_row[3]).grid(row=count, column=4, sticky=W, padx=(7, 7))
        Entry(frame).grid(row=count, column=5, padx=(0, 7), pady=(3, 3))
        Entry(frame).grid(row=count, column=6, padx=(0, 7), pady=(3, 3))
        Label(frame, textvariable=v).grid(row=count, column=7, sticky=W, padx=(0, 7))
        Button(frame, text='OK', state=NORMAL, command=lambda: [v.set("Concluído"), conclude_call(put_row[3])]).grid(row=count, column=8, padx=(0, 7), pady=(3, 3))


class App(threading.Thread):

    def __init__(self, tk_root, count, selected_frame, base):
        self.root = tk_root
        self.count = count
        self.frame = selected_frame
        self.data = base
        self.loop_active = False
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        tempo = time.ctime(os.path.getmtime(tools.path_vendas))
        with open(tools.path_vendas, 'r') as looking_at:
            reader = csv.reader(looking_at)
            self.loop_active = True
            while self.loop_active:
                self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
                if time.ctime(os.path.getmtime(tools.path_vendas)) != tempo:
                    tempo = time.ctime(os.path.getmtime(tools.path_vendas))
                    for row in reader:
                        if row not in self.data:
                            print(row)
                            self.data.append(row)
                            put_label(self.frame, row, self.count)
                            self.count = + 1

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.loop_active = False
            self.root.quit()
            self.root.update()


def down(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=1200, height=600)


root = Tk()
root.title('MaxiDesk')
root.geometry('1200x400+' + str(int(GetSystemMetrics(0) / 2 - 600)) + '+' + str(int(GetSystemMetrics(1) / 2 - 200)))
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
            put_label(second_frame, row, i)
            i += 1

scroll = Scrollbar(principal_frame, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)
scroll.pack(side='right', fill=Y)
canvas.pack()
canvas.create_window((0, 0), window=second_frame)
second_frame.bind('<Configure>', down)

APP = App(root, i, second_frame, data)
root.mainloop()
