import tools
from tkinter import *
from win32api import GetSystemMetrics


def printing_id(id):
    title = Label(root, text= "sua ordem de serviço é: %05d\nGuarde o número, pois somente com ele, você conseguirá acompanhar o seu chamado" % id,
                  fg='firebrick', font=("Malgun Gothic", 12, "bold")).grid(row=5, column=1, sticky=W, columnspan=5, padx=(175,0), pady=(25,0))


root = Tk()
root.title('MaxiDesk')
root.geometry('1000x300+' + str(int(GetSystemMetrics(0)/2 - 500)) + '+' + str(int(GetSystemMetrics(1)/2 - 250)))
root.resizable(False, False)

choices = {'T.I.', 'Trade', 'Vendas'}
tkvar = StringVar(root)
tkvar.set('T.I.')

namelab = Label(root, text="Name", font=("Malgun Gothic", 16, "bold"))
namelab.grid(row=0, column=1, padx=(55, 15), pady=(75,0))
name = Entry(root, width=20)
name.grid(row=1, column=1,padx=(55, 15) )

problemlab = Label(root, text="Problem", font=("Malgun Gothic", 16, "bold"))
problemlab.grid(row=0, column=2, pady=(75,0))
problem = Entry(root, width=50)
problem.grid(row=1, column=2)

choices = {'T.I.', 'Trade', 'Vendas', 'Marketing', 'Compras', 'Financeiro', 'Fiscal', 'Diretoria', 'Sac', 'Qualidade', 'PCP', 'Laboratório', 'Manutenção', 'Produção'}
tkvar = StringVar(root)
tkvar.set('T.I.')
dptolab = Label(root, text="Department", font=("Malgun Gothic", 16, "bold"))
dptolab.grid(row=0, column=3, pady=(75,0))
dpto = OptionMenu(root, tkvar, *choices)
dpto.config(width=20)
dpto.grid(row=1, column=3, padx=(15, 15))

b = Button(root, text="Confirm", font=("Malgun Gothic", 16, "bold"), width=20,
           command=lambda: [printid(tools.write_calling(tools.path_vendas, name.get(), problem.get(), tkvar.get()))
               ,name.delete(0, END), problem.delete(0, END)]).grid(row=0, column=5, rowspan=2, pady=(80,0))

root.mainloop()