from tkinter import *

def data():
    for i in range(50):
       Label(frame,text=i).grid(row=i,column=0)
       Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame,text="..........").grid(row=i,column=2)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=400)

root=Tk()
sizex = 600
sizey = 400
posx  = 250
posy  = 150
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,width=600,height=400,bg='blue')
myframe.place(x=0, y=0)

canvas=Canvas(myframe, bg = 'red', height=400, width=sizex)

frame=Frame(canvas)
data()
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left", fill=BOTH)
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

root.mainloop()