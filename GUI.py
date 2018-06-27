import tools
from tkinter import *
from win32api import GetSystemMetrics

root = Tk()
root.title('MaxiDesk')
root.geometry('1000x300+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))

problemlab = Label(root, text="Problem", font=("Malgun Gothic", 16, "bold"))
problemlab.grid(row=0, column=1)
problem = Entry(root)
problem.grid(row=1, column=1, padx=(15, 15))

namelab = Label(root, text="Name", font=("Malgun Gothic", 16, "bold"))
namelab.grid(row=0, column=2)
name = Entry(root)
name.grid(row=1, column=2)

dptolab = Label(root, text="Dpto", font=("Malgun Gothic", 16, "bold"))
dptolab.grid(row=0, column=3)
dpto = Entry(root)
dpto.grid(row=1, column=3, padx=(15, 15))

b = Button(root, text="Confirmar", font=("Malgun Gothic", 16, "bold"), width = 20,
           command=lambda: [tools.write_calling(tools.path_vendas, name.get(), problem.get(), dpto.get()),
                            name.delete(0, END), problem.delete(0, END), dpto.delete(0, END)]).grid(row=3, column = 5)

root.mainloop()