import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing():
    return messagebox.askokcancel("Quit", "Do you want to quit?")


if root.protocol("WM_DELETE_WINDOW", on_closing):
    root.destroy()

root.mainloop()